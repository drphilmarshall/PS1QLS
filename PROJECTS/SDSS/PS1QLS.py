#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_validation import train_test_split
from astroML.density_estimation import XDGMM
from astropy.io import fits
from sklearn.ensemble import RandomForestClassifier
from sklearn import grid_search
from sklearn import metrics
import triangle
import pickle

lQSO_prior = .06007 #~1800 in a 30,000 sq deg PS1-like survey according to OM10 TODO: what is the actual PS1 depth?
dud_prior = 12300 # reciprocal number of objects in PS1 data sample from eric 

def listify(covmat,length):
    if length <= 1:
        return covmat[:,:,np.newaxis]
    else:
        covmatlist = np.dstack((covmat,covmat))
        while covmatlist.shape[2] < length:
            covmatlist = np.dstack((covmatlist,covmat))
    return covmatlist.transpose()

class Dataset(object):

    def __init__(self,data,truth=None,text=None):
        self.data = data
        self.text = text
        self.truth=truth
        self.nFeatures = data.shape[1]
        self.covmat = .9*np.identity(self.nFeatures)+.1*np.ones(self.nFeatures)
        return
        
    def noisify(self):
        perturbations = np.random.multivariate_normal(np.zeros(self.nFeatures),self.covmat,size=self.data.shape[0])
        self.truedata = self.data
        self.data = self.data + perturbations
        return
        
    def resample_from(self,xd_classifier):
        self.resampled = np.concatenate((xd_classifier.lQSO_model.sample(np.sum(self.truth)), \
                                         xd_classifier.dud_model.sample(np.sum(1-self.truth))),axis=0)
        return
    
    def plot(self):
        if hasattr(self,'truedata'):
            if hasattr(self,'resampled'):
                fig1 = triangle.corner(self.truedata,labels=self.text)
                _ = triangle.corner(self.data,fig=fig1,labels=self.text,color='r')
                _ = triangle.corner(self.resampled,fig=fig1,color='b',labels=self.text)
                fig1.suptitle('Everything')
                return
            fig1 = triangle.corner(self.truedata,labels=self.text)
            _ = triangle.corner(self.data,fig=fig1,labels=self.text,color='r')
            fig1.suptitle('Noisy Data over Truth')
            return
        if self.truth is not None:
            fig1 = triangle.corner(self.data[self.truth==0],truths=self.data[self.truth==1],truth_color='b',labels=self.text)
            #fig1 = triangle.corner(self.data[self.truth==1],color='b',fig=fig1,plot_datapoints=True,plot_contours=False,labels=self.text)
            fig1.suptitle('Cornerplot for Raw Data')
        else:
            fig1 = triangle.corner(self.data,labels=self.text)
            fig1.suptitle('Cornerplot for Raw Data')
        return

class Classifier(object):

    def __init__(self,algorithm='XD',n_comp = 20):
        if algorithm == 'XD':
            self.algorithm='XD'
            self.lQSO_model = XDGMM(n_components=n_comp,verbose=True)
            self.dud_model = XDGMM(n_components=n_comp,verbose=True)
        elif algorithm == 'RandomForest':
            self.algorithm = 'RandomForest'
            self.trialRF = RandomForestClassifier()
            self.RF_params = {'n_estimators':(10,50,200),"max_features": ["auto",2,4],
                          'criterion':["gini","entropy"],"min_samples_leaf": [1,2]}
        return
    
    def train(self,train,truth,covmat=1):
        if self.algorithm == 'XD':
            self.XDtrain(train,truth,covmat)
        elif self.algorithm == 'RandomForest':
            self.RFtrain(train,truth)
        return
    
    def RFtrain(self,train,truth):
        tunedRF = grid_search.GridSearchCV(self.trialRF, self.RF_params, score_func=metrics.accuracy_score,\
                                    n_jobs = -1, cv = 3,verbose=1)
        self.optRF = tunedRF.fit(train, truth)
        return
    
    def XDtrain(self,train,truth,covmat=1):
        self.lQSO_model.fit(train[truth==1], listify(covmat,np.sum(truth)))
        self.dud_model.fit(train[truth==0], listify(covmat,np.sum(1-truth)))
        return
    
    def test(self,test,covmat=1):
        if self.algorithm == 'XD':
            self.XDprobs(test,covmat)
        elif self.algorithm == 'RandomForest':
            self.RFprobs(test)
        return
    
    def RFprobs(self,test):
        self.dud_probs = self.optRF.predict_proba(test)[:,0]
        self.lQSO_probs = self.optRF.predict_proba(test)[:,1]
        return
    
    def XDprobs(self,test,covmat):
        lQSO_like = np.sum(np.exp(self.lQSO_model.logprob_a(test, listify(covmat,test.shape[0]))),axis=1)
        dud_like= np.sum(np.exp(self.dud_model.logprob_a(test, listify(covmat,test.shape[0]))),axis=1)
        self.lQSO_probs = (lQSO_like * lQSO_prior) / (lQSO_like * lQSO_prior + dud_like * dud_prior)
        self.dud_probs =  (dud_like  *  dud_prior) / (lQSO_like * lQSO_prior + dud_like * dud_prior)
        return
    
    def make_roc(self,truth):
        fpr, tpr, _ = metrics.roc_curve(truth,self.lQSO_probs,pos_label=1)
        plt.title('ROC Curve')
        plt.plot(fpr,tpr,'b--')
        plt.xlabel('FPR')
        plt.ylabel('TPR')
        return fpr, tpr
    
    def make_pc_plot(self, truth, abundance=1e-3):
        """
        Plots purity against completeness, assuming a natural abundance of lenses.
        
        Parameters
        ----------
        truth: ndarray
            True labels for the test dataset objects.
        abundance: float
            Fraction of all objects in the expected parent dataset that are actually lenses.
        // code starts here
        
        purity, completeness, _ = sklearn.metrics.precision_recall_curve(truth, self.lQSO_probs, pos_label=1)
        plt.title('Purity-Completeness Curve')
        plt.plot(purity,completeness,'b--')
        plt.xlabel('purity')
        plt.ylabel('completeness')
        return completeness, purity
        // code ends here
        Returns
        -------
        c: ndarray
            Array of completeness values
        p: ndarray
            Array of purity values
            
        Notes
        -----
        Definition of Purity : (True Positive/(True Positive+False Positive))
        Definition of Completeness : (True Positive/(True Positive+False Negative))
        """
        pass
        return
    
    def save(self,pkl_fname='classifiers.pkl'):
        outfile = open(pkl_fname,'wb')
        outDict = {}
        if hasattr(self,'lQSO_model'):
            outDict.update({'lQSO_model':self.lQSO_model})
        if hasattr(self,'dud_model'):
            outDict.update({'dud_model':self.dud_model})
        if hasattr(self,'optRF'):
            outDict.update({'optRF':self.optRF})
        pickle.dump(outDict,outfile)
        outfile.close()
        return
    
    def load(self,pkl_fname='classifiers.pkl'):
        pkl_in = open(pkl_fname,'rb')
        inDict = pickle.load(pkl_in)
        pkl_in.close()
        if 'lQSO_model' in inDict.keys():
            self.lQSO_model = inDict['lQSO_model']
        if 'dud_model' in inDict.keys():
            self.dud_model = inDict['dud_model']
        if 'optRF' in inDict.keys():
            self.optRF = inDict['optRF']
        return
