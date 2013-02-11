<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  
  

  
      



  

  <head>
    <title>
      /trunk/psModules/src/objects/pmSourceMasks.h – Pan-STARRS IPP
    </title>
        <link rel="search" href="/trac/ipp/search" />
        <link rel="help" href="/trac/ipp/wiki/TracGuide" />
        <link rel="alternate" href="/trac/ipp/browser/trunk/psModules/src/objects/pmSourceMasks.h?format=txt" type="text/plain" title="Plain Text" /><link rel="alternate" href="/trac/ipp/export/32198/trunk/psModules/src/objects/pmSourceMasks.h" type="text/x-chdr; charset=iso-8859-15" title="Original Format" />
        <link rel="up" href="/trac/ipp/browser/trunk/psModules/src/objects" title="Parent directory" />
        <link rel="start" href="/trac/ipp/wiki" />
        <link rel="stylesheet" href="/trac/ipp/chrome/common/css/trac.css" type="text/css" /><link rel="stylesheet" href="/trac/ipp/chrome/common/css/code.css" type="text/css" /><link rel="stylesheet" href="/trac/ipp/pygments/trac.css" type="text/css" /><link rel="stylesheet" href="/trac/ipp/chrome/common/css/browser.css" type="text/css" />
        <link rel="shortcut icon" href="/trac/ipp/chrome/common/trac.ico" type="image/x-icon" />
        <link rel="icon" href="/trac/ipp/chrome/common/trac.ico" type="image/x-icon" />
      <link type="application/opensearchdescription+xml" rel="search" href="/trac/ipp/search/opensearch" title="Search Pan-STARRS IPP" />
    <script type="text/javascript" src="/trac/ipp/chrome/common/js/jquery.js"></script><script type="text/javascript" src="/trac/ipp/chrome/common/js/trac.js"></script><script type="text/javascript" src="/trac/ipp/chrome/common/js/search.js"></script><script type="text/javascript" src="/trac/ipp/chrome/tracsectionedit/js/tracsectionedit.js"></script>
    <!--[if lt IE 7]>
    <script type="text/javascript" src="/trac/ipp/chrome/common/js/ie_pre7_hacks.js"></script>
    <![endif]-->
    <script type="text/javascript">
      jQuery(document).ready(function($) {
        $("#jumploc input").hide();
        $("#jumploc select").change(function () {
          this.parentNode.parentNode.submit();
        })
      });
    </script>
        <link rel="stylesheet" type="text/css" href="/trac/ipp/chrome/site/ps.css" />
    </head>
        <body>
                <div id="toplevel">
                <div id="banner">
                    <!-- <img src="${href.chrome('site/logo.jpg')}" /> -->
		    <img src="http://pan-starrs.ifa.hawaii.edu/public/logos/PanSTARRS4c_180.jpg" height="75" />
      <form id="search" action="/trac/ipp/search" method="get">
                <div>
          <label for="proj-search">Search:</label>
          <input type="text" id="proj-search" name="q" size="18" value="" />
          <input type="submit" value="Search" />
                </div>
      </form>
                <div id="metanav" class="nav">
    <ul>
      <li class="first"><a href="/trac/ipp/login">Login</a></li><li><a href="/trac/ipp/prefs">Preferences</a></li><li><a href="/trac/ipp/wiki/TracGuide">Help/Guide</a></li><li class="last"><a href="/trac/ipp/about">About Trac</a></li>
    </ul>
                </div>
                </div>
                <div id="mainnav" class="nav">
    <ul>
      <li class="first"><a href="/trac/ipp/wiki">Wiki</a></li><li><a href="/trac/ipp/timeline">Timeline</a></li><li><a href="/trac/ipp/roadmap">Roadmap</a></li><li class="active"><a href="/trac/ipp/browser">Browse Source</a></li><li><a href="/trac/ipp/report">View Tickets</a></li><li class="last"><a href="/trac/ipp/search">Search</a></li>
    </ul>
                </div>
                <div id="main">
                <div id="ctxtnav" class="nav">
        <h2>Context Navigation</h2>
          <ul>
            <li class="first "><a href="/trac/ipp/changeset/31670/trunk/psModules/src/objects/pmSourceMasks.h">Last Change</a></li><li><a href="/trac/ipp/browser/trunk/psModules/src/objects/pmSourceMasks.h?annotate=blame&amp;rev=31670" title="Annotate each line with the last changed revision (this can be time consuming...)">Annotate</a></li><li class="last"><a href="/trac/ipp/log/trunk/psModules/src/objects/pmSourceMasks.h">Revision Log</a></li>
          </ul>
        <hr />
                </div>
                <div id="content-side">
                    
        <span>IPP Software</span>
        <ul>
        <li>
            <a href="/trac/ipp/">IPP Main Page</a>
        </li>
        <li>
            <a href="/trac/ipp/wiki/IPP_Description">IPP Description</a>
        </li>
        <li>
            <a href="/trac/ipp/wiki/IPP_Installation">IPP Installation</a>
        </li>
        <li>
            <a href="http://ipp0022.ifa.hawaii.edu/ippDocs">IPP Doxygen</a>
        </li>
        <li>
            <a href="/trac/ipp/wiki/IPP_Manuals">IPP Manuals</a>
        </li>
        <li>
            <a href="/trac/ipp/wiki/Index">IPP Wiki Index</a>
        </li>
</ul>
        <span>Navigation</span>
        <ul>
        <li>
            <a href="http://panstarrs.ifa.hawaii.edu">PS Home</a>
        </li>
        <li>
            <a href="http://panstarrs.ifa.hawaii.edu/project">PS Project *</a>
        </li>
        <li>
            <a href="http://panstarrs.ifa.hawaii.edu/project/IPP">Old IPP Home *</a>
        </li>
        <li>
            <a href="http://ps1sc.org ">PS1SC Home</a>
        </li>
        <li>
            <a href="http://ps1sc.ifa.hawaii.edu/PS1wiki/index.php/Main_Page">PS1SC Wiki *</a>
        </li>
</ul>
        <span>Tools</span>
        <ul>
        <li>
            <a href="/trac/ipp/wiki/FAQ">FAQ pages</a>
        </li>
        <li>
            <a href="http://svn.pan-starrs.ifa.hawaii.edu/trac/ipp/report">IPP Trac Tickets</a>
        </li>
        <li>
            <a href="http://svn.pan-starrs.ifa.hawaii.edu/trac/ipp/browser">IPP SVN Browser</a>
        </li>
        <li>
            <a href="/trac/ipp/wiki/TracGuide">Wiki Help</a>
        </li>
</ul>
        <span>IPP Links</span>
        <ul>
        <li>
            <a href="http://ippdb01.ifa.hawaii.edu/ippMonitor">ippMonitor@MHPCC*</a>
        </li>
        <li>
            <a href="http://ipp0012.ifa.hawaii.edu/ippMonitor">ippMonitor@Manoa*</a>
        </li>
        <li>
            <a href="http://pstamp.ipp.ifa.hawaii.edu/request.php">PStamp Server*</a>
        </li>
        <li>
            <a href="http://ganglia.pan-starrs.ifa.hawaii.edu">Ganglia*</a>
        </li>
</ul>
        <span>Communication</span>
        <ul>
        <li>
            <a href="/trac/ipp/wiki/Ps-ipp-users">IPP Users maillist</a>
        </li>
        <li>
            <a href="http://panstarrs.ifa.hawaii.edu/project/mail">email lists (PS) *</a>
        </li>
        <li>
            <a href="http://ps1sc.ifa.hawaii.edu/PS1wiki/index.php/DRAVG">DRAV Info *</a>
        </li>
        <li>
            <a href="http://ipp0022.ifa.hawaii.edu/ippBlog">IPP Blog</a>
        </li>
</ul>
        <span>Pan-STARRS Links</span>
        <ul>
        <li>
            <a href="https://svn.ifa.hawaii.edu/">Camera</a>
        </li>
        <li>
            <a href="http://ps1wiki.ifa.hawaii.edu/trac">Summit Wiki</a>
        </li>
        <li>
            <a href="http://banana.ifa.hawaii.edu/">Haleakala Site Pages</a>
        </li>
        <li>
            <a href="http://mkwc.ifa.hawaii.edu/">Mauna Kea Weather Center</a>
        </li>
        <li>
            <a href="http://www.ifa.hawaii.edu/">IfA</a>
        </li>
        <li>
            <a href="/trac/ipp/wiki/RoboDIMM">PS1 Seeing</a>
        </li>
</ul>
* -- restricted access

                </div>
                <div id="content" class="browser">
      <h1>
    <a class="pathentry first" title="Go to root directory" href="/trac/ipp/browser">root</a><span class="pathentry sep">/</span><a class="pathentry" title="View trunk" href="/trac/ipp/browser/trunk">trunk</a><span class="pathentry sep">/</span><a class="pathentry" title="View psModules" href="/trac/ipp/browser/trunk/psModules">psModules</a><span class="pathentry sep">/</span><a class="pathentry" title="View src" href="/trac/ipp/browser/trunk/psModules/src">src</a><span class="pathentry sep">/</span><a class="pathentry" title="View objects" href="/trac/ipp/browser/trunk/psModules/src/objects">objects</a><span class="pathentry sep">/</span><a class="pathentry" title="View pmSourceMasks.h" href="/trac/ipp/browser/trunk/psModules/src/objects/pmSourceMasks.h">pmSourceMasks.h</a>
        <br />
  </h1>
                <div id="jumprev">
        <form action="" method="get">
                <div>
            <label for="rev">
              View revision:</label>
            <input type="text" id="rev" name="rev" size="6" />
                </div>
        </form>
                </div>
                <div id="jumploc">
        <form action="" method="get">
                <div class="buttons">
            <label for="preselected">Visit:</label>
            <select id="preselected" name="preselected">
              <option selected="selected"></option>
              <optgroup label="branches">
                <option value="/trac/ipp/browser/trunk">trunk</option><option value="/trac/ipp/browser/branches/bills_081204">branches/bills_081204</option><option value="/trac/ipp/browser/branches/cnb_branches">branches/cnb_branches</option><option value="/trac/ipp/browser/branches/czw_branch">branches/czw_branch</option><option value="/trac/ipp/browser/branches/eam_branches">branches/eam_branches</option><option value="/trac/ipp/browser/branches/haf_branches">branches/haf_branches</option><option value="/trac/ipp/browser/branches/ipp-1-X">branches/ipp-1-X</option><option value="/trac/ipp/browser/branches/ipp-2-6-1">branches/ipp-2-6-1</option><option value="/trac/ipp/browser/branches/ipp-magic-v0">branches/ipp-magic-v0</option><option value="/trac/ipp/browser/branches/jh_branches">branches/jh_branches</option><option value="/trac/ipp/browser/branches/meh_branches">branches/meh_branches</option><option value="/trac/ipp/browser/branches/mwv">branches/mwv</option><option value="/trac/ipp/browser/branches/neb_distrib_20081210">branches/neb_distrib_20081210</option><option value="/trac/ipp/browser/branches/neb_single_20081210">branches/neb_single_20081210</option><option value="/trac/ipp/browser/branches/ohana">branches/ohana</option><option value="/trac/ipp/browser/branches/pap">branches/pap</option><option value="/trac/ipp/browser/branches/pap_old_efficiency">branches/pap_old_efficiency</option><option value="/trac/ipp/browser/branches/pap_stack">branches/pap_stack</option><option value="/trac/ipp/browser/branches/pitts_branches">branches/pitts_branches</option><option value="/trac/ipp/browser/branches/ppTranslate">branches/ppTranslate</option><option value="/trac/ipp/browser/branches/rhl_branches">branches/rhl_branches</option><option value="/trac/ipp/browser/branches/sc_branches">branches/sc_branches</option><option value="/trac/ipp/browser/branches/simmosaic_branches">branches/simmosaic_branches</option><option value="/trac/ipp/browser/branches/simtest_nebulous_branches">branches/simtest_nebulous_branches</option><option value="/trac/ipp/browser/branches/sj_branches">branches/sj_branches</option><option value="/trac/ipp/browser/branches/tap_branches">branches/tap_branches</option><option value="/trac/ipp/browser/branches/wiyn_branches">branches/wiyn_branches</option>
              </optgroup><optgroup label="tags">
                <option value="/trac/ipp/browser/tags/before_diffwork_081213?rev=21063">tags/before_diffwork_081213</option><option value="/trac/ipp/browser/tags/cnb_tags?rev=23136">tags/cnb_tags</option><option value="/trac/ipp/browser/tags/doc?rev=27971">tags/doc</option><option value="/trac/ipp/browser/tags/eam_tags?rev=22417">tags/eam_tags</option><option value="/trac/ipp/browser/tags/ifa-tree-is-primary?rev=14890">tags/ifa-tree-is-primary</option><option value="/trac/ipp/browser/tags/ipp-1-X?rev=22674">tags/ipp-1-X</option><option value="/trac/ipp/browser/tags/ipp-2-6-1-0?rev=18803">tags/ipp-2-6-1-0</option><option value="/trac/ipp/browser/tags/ipp-20100516?rev=28071">tags/ipp-20100516</option><option value="/trac/ipp/browser/tags/ipp-20100525?rev=28147">tags/ipp-20100525</option><option value="/trac/ipp/browser/tags/ipp-20100602?rev=28251">tags/ipp-20100602</option><option value="/trac/ipp/browser/tags/ipp-20100610?rev=28374">tags/ipp-20100610</option><option value="/trac/ipp/browser/tags/ipp-20100616?rev=28410">tags/ipp-20100616</option><option value="/trac/ipp/browser/tags/ipp-20100623?rev=29030">tags/ipp-20100623</option><option value="/trac/ipp/browser/tags/ipp-20100701?rev=28945">tags/ipp-20100701</option><option value="/trac/ipp/browser/tags/ipp-20100823?rev=29525">tags/ipp-20100823</option><option value="/trac/ipp/browser/tags/ipp-20101029?rev=29901">tags/ipp-20101029</option><option value="/trac/ipp/browser/tags/ipp-20101206?rev=30046">tags/ipp-20101206</option><option value="/trac/ipp/browser/tags/ipp-20101215?rev=30687">tags/ipp-20101215</option><option value="/trac/ipp/browser/tags/ipp-20110218?rev=31143">tags/ipp-20110218</option><option value="/trac/ipp/browser/tags/ipp-20110406?rev=31426">tags/ipp-20110406</option><option value="/trac/ipp/browser/tags/ipp-20110505?rev=31646">tags/ipp-20110505</option><option value="/trac/ipp/browser/tags/ipp-20110621?rev=31679">tags/ipp-20110621</option><option value="/trac/ipp/browser/tags/ipp-20110622?rev=32198">tags/ipp-20110622</option><option value="/trac/ipp/browser/tags/ipp-docs?rev=22204">tags/ipp-docs</option><option value="/trac/ipp/browser/tags/ipp-magic-v0-0?rev=21460">tags/ipp-magic-v0-0</option><option value="/trac/ipp/browser/tags/ipp-magic-v1-0?rev=26069">tags/ipp-magic-v1-0</option><option value="/trac/ipp/browser/tags/ippdvo-20110427?rev=31652">tags/ippdvo-20110427</option><option value="/trac/ipp/browser/tags/jh_tags?rev=22352">tags/jh_tags</option><option value="/trac/ipp/browser/tags/neb_distrib_20081210_00?rev=20891">tags/neb_distrib_20081210_00</option><option value="/trac/ipp/browser/tags/ohana?rev=23446">tags/ohana</option><option value="/trac/ipp/browser/tags/owen-01?rev=10380">tags/owen-01</option><option value="/trac/ipp/browser/tags/pap_tags?rev=22326">tags/pap_tags</option><option value="/trac/ipp/browser/tags/rhl_tags?rev=22319">tags/rhl_tags</option><option value="/trac/ipp/browser/tags/sj_tags?rev=23262">tags/sj_tags</option>
              </optgroup>
            </select>
            <input type="submit" value="Go!" title="Jump to the chosen preselected path" />
                </div>
        </form>
                </div>
      <table id="info" summary="Revision info">
        <tr>
          <th scope="col">
            Revision <a href="/trac/ipp/changeset/31670">31670</a>, <span title="4742 bytes">4.6 KB</span>
            (checked in by eugene, <a class="timeline" href="/trac/ipp/timeline?from=2011-06-22T00%3A48%3A29Z-1000&amp;precision=second" title="2011-06-22T00:48:29Z-1000 in Timeline">2 months</a> ago)
          </th>
        </tr>
        <tr>
          <td class="message searchable">
              <p>
merge from trunk : various minor issues (kron radii; I/O fixes)<br />
</p>
          </td>
        </tr>
      </table>
                <div id="preview" class="searchable">
    <table class="code"><thead><tr><th class="lineno" title="Line numbers">Line</th><th class="content"> </th></tr></thead><tbody><tr><th id="L1"><a href="#L1">1</a></th><td><span class="cp">#ifndef PM_SOURCE_MASKS_H</span></td></tr><tr><th id="L2"><a href="#L2">2</a></th><td><span class="cp">#define PM_SOURCE_MASKS_H</span></td></tr><tr><th id="L3"><a href="#L3">3</a></th><td><span class="cp"></span></td></tr><tr><th id="L4"><a href="#L4">4</a></th><td><span class="c">// Bit flags to distinguish analysis results</span></td></tr><tr><th id="L5"><a href="#L5">5</a></th><td><span class="c">// When adding to or subtracting from this list, please also modify pmSourceMaskHeader</span></td></tr><tr><th id="L6"><a href="#L6">6</a></th><td><span class="c"></span><span class="k">typedef</span> <span class="k">enum</span> <span class="p">{</span></td></tr><tr><th id="L7"><a href="#L7">7</a></th><td>    PM_SOURCE_MODE_DEFAULT          <span class="o">=</span> <span class="mh">0x00000000</span><span class="p">,</span> <span class="c">///&lt; Initial value: resets all bits</span></td></tr><tr><th id="L8"><a href="#L8">8</a></th><td><span class="c"></span>    PM_SOURCE_MODE_PSFMODEL         <span class="o">=</span> <span class="mh">0x00000001</span><span class="p">,</span> <span class="c">///&lt; Source fitted with a psf model (linear or non-linear)</span></td></tr><tr><th id="L9"><a href="#L9">9</a></th><td><span class="c"></span>    PM_SOURCE_MODE_EXTMODEL         <span class="o">=</span> <span class="mh">0x00000002</span><span class="p">,</span> <span class="c">///&lt; Source fitted with an extended-source model</span></td></tr><tr><th id="L10"><a href="#L10">10</a></th><td><span class="c"></span>    PM_SOURCE_MODE_FITTED           <span class="o">=</span> <span class="mh">0x00000004</span><span class="p">,</span> <span class="c">///&lt; Source fitted with non-linear model (PSF or EXT; good or bad)</span></td></tr><tr><th id="L11"><a href="#L11">11</a></th><td><span class="c"></span>    PM_SOURCE_MODE_FAIL             <span class="o">=</span> <span class="mh">0x00000008</span><span class="p">,</span> <span class="c">///&lt; Fit (non-linear) failed (non-converge, off-edge, run to zero)</span></td></tr><tr><th id="L12"><a href="#L12">12</a></th><td><span class="c"></span>    PM_SOURCE_MODE_POOR             <span class="o">=</span> <span class="mh">0x00000010</span><span class="p">,</span> <span class="c">///&lt; Fit succeeds, but low-SN, high-Chisq, or large (for PSF -- drop?)</span></td></tr><tr><th id="L13"><a href="#L13">13</a></th><td><span class="c"></span>    PM_SOURCE_MODE_PAIR             <span class="o">=</span> <span class="mh">0x00000020</span><span class="p">,</span> <span class="c">///&lt; Source fitted with a double psf</span></td></tr><tr><th id="L14"><a href="#L14">14</a></th><td><span class="c"></span>    PM_SOURCE_MODE_PSFSTAR          <span class="o">=</span> <span class="mh">0x00000040</span><span class="p">,</span> <span class="c">///&lt; Source used to define PSF model</span></td></tr><tr><th id="L15"><a href="#L15">15</a></th><td><span class="c"></span>    PM_SOURCE_MODE_SATSTAR          <span class="o">=</span> <span class="mh">0x00000080</span><span class="p">,</span> <span class="c">///&lt; Source model peak is above saturation</span></td></tr><tr><th id="L16"><a href="#L16">16</a></th><td><span class="c"></span>    PM_SOURCE_MODE_BLEND            <span class="o">=</span> <span class="mh">0x00000100</span><span class="p">,</span> <span class="c">///&lt; Source is a blend with other sources</span></td></tr><tr><th id="L17"><a href="#L17">17</a></th><td><span class="c"></span>    PM_SOURCE_MODE_EXTERNAL         <span class="o">=</span> <span class="mh">0x00000200</span><span class="p">,</span> <span class="c">///&lt; Source based on supplied input position</span></td></tr><tr><th id="L18"><a href="#L18">18</a></th><td><span class="c"></span>    PM_SOURCE_MODE_BADPSF           <span class="o">=</span> <span class="mh">0x00000400</span><span class="p">,</span> <span class="c">///&lt; Failed to get good estimate of object's PSF</span></td></tr><tr><th id="L19"><a href="#L19">19</a></th><td><span class="c"></span>    PM_SOURCE_MODE_DEFECT           <span class="o">=</span> <span class="mh">0x00000800</span><span class="p">,</span> <span class="c">///&lt; Source is thought to be a defect</span></td></tr><tr><th id="L20"><a href="#L20">20</a></th><td><span class="c"></span>    PM_SOURCE_MODE_SATURATED        <span class="o">=</span> <span class="mh">0x00001000</span><span class="p">,</span> <span class="c">///&lt; Source is thought to be saturated pixels (bleed trail)</span></td></tr><tr><th id="L21"><a href="#L21">21</a></th><td><span class="c"></span>    PM_SOURCE_MODE_CR_LIMIT         <span class="o">=</span> <span class="mh">0x00002000</span><span class="p">,</span> <span class="c">///&lt; Source has crNsigma above limit</span></td></tr><tr><th id="L22"><a href="#L22">22</a></th><td><span class="c"></span>    PM_SOURCE_MODE_EXT_LIMIT        <span class="o">=</span> <span class="mh">0x00004000</span><span class="p">,</span> <span class="c">///&lt; Source has extNsigma above limit</span></td></tr><tr><th id="L23"><a href="#L23">23</a></th><td><span class="c"></span>    PM_SOURCE_MODE_MOMENTS_FAILURE  <span class="o">=</span> <span class="mh">0x00008000</span><span class="p">,</span> <span class="c">///&lt; could not measure the moments</span></td></tr><tr><th id="L24"><a href="#L24">24</a></th><td><span class="c"></span>    PM_SOURCE_MODE_SKY_FAILURE      <span class="o">=</span> <span class="mh">0x00010000</span><span class="p">,</span> <span class="c">///&lt; could not measure the local sky</span></td></tr><tr><th id="L25"><a href="#L25">25</a></th><td><span class="c"></span>    PM_SOURCE_MODE_SKYVAR_FAILURE   <span class="o">=</span> <span class="mh">0x00020000</span><span class="p">,</span> <span class="c">///&lt; could not measure the local sky variance</span></td></tr><tr><th id="L26"><a href="#L26">26</a></th><td><span class="c"></span>    PM_SOURCE_MODE_BELOW_MOMENTS_SN <span class="o">=</span> <span class="mh">0x00040000</span><span class="p">,</span> <span class="c">///&lt; moments not measured due to low S/N</span></td></tr><tr><th id="L27"><a href="#L27">27</a></th><td><span class="c"></span>    PM_SOURCE_MODE_BIG_RADIUS       <span class="o">=</span> <span class="mh">0x00100000</span><span class="p">,</span> <span class="c">///&lt; poor moments for small radius, try large radius</span></td></tr><tr><th id="L28"><a href="#L28">28</a></th><td><span class="c"></span>    PM_SOURCE_MODE_AP_MAGS          <span class="o">=</span> <span class="mh">0x00200000</span><span class="p">,</span> <span class="c">///&lt; source has an aperture magnitude</span></td></tr><tr><th id="L29"><a href="#L29">29</a></th><td><span class="c"></span>    PM_SOURCE_MODE_BLEND_FIT        <span class="o">=</span> <span class="mh">0x00400000</span><span class="p">,</span> <span class="c">///&lt; source was fitted as a blend</span></td></tr><tr><th id="L30"><a href="#L30">30</a></th><td><span class="c"></span>    PM_SOURCE_MODE_EXTENDED_FIT     <span class="o">=</span> <span class="mh">0x00800000</span><span class="p">,</span> <span class="c">///&lt; full extended fit was used</span></td></tr><tr><th id="L31"><a href="#L31">31</a></th><td><span class="c"></span>    PM_SOURCE_MODE_EXTENDED_STATS   <span class="o">=</span> <span class="mh">0x01000000</span><span class="p">,</span> <span class="c">///&lt; extended aperture stats calculated</span></td></tr><tr><th id="L32"><a href="#L32">32</a></th><td><span class="c"></span>    PM_SOURCE_MODE_LINEAR_FIT       <span class="o">=</span> <span class="mh">0x02000000</span><span class="p">,</span> <span class="c">///&lt; source fitted with the linear fit</span></td></tr><tr><th id="L33"><a href="#L33">33</a></th><td><span class="c"></span>    PM_SOURCE_MODE_NONLINEAR_FIT    <span class="o">=</span> <span class="mh">0x04000000</span><span class="p">,</span> <span class="c">///&lt; source fitted with the non-linear fit</span></td></tr><tr><th id="L34"><a href="#L34">34</a></th><td><span class="c"></span>    PM_SOURCE_MODE_RADIAL_FLUX      <span class="o">=</span> <span class="mh">0x08000000</span><span class="p">,</span> <span class="c">///&lt; radial flux measurements calculated</span></td></tr><tr><th id="L35"><a href="#L35">35</a></th><td><span class="c"></span>    PM_SOURCE_MODE_SIZE_SKIPPED     <span class="o">=</span> <span class="mh">0x10000000</span><span class="p">,</span> <span class="c">///&lt; size could not be determined</span></td></tr><tr><th id="L36"><a href="#L36">36</a></th><td><span class="c"></span>    PM_SOURCE_MODE_ON_SPIKE         <span class="o">=</span> <span class="mh">0x20000000</span><span class="p">,</span> <span class="c">///&lt; peak lands on diffraction spike</span></td></tr><tr><th id="L37"><a href="#L37">37</a></th><td><span class="c"></span>    PM_SOURCE_MODE_ON_GHOST         <span class="o">=</span> <span class="mh">0x40000000</span><span class="p">,</span> <span class="c">///&lt; peak lands on ghost or glint</span></td></tr><tr><th id="L38"><a href="#L38">38</a></th><td><span class="c"></span>    PM_SOURCE_MODE_OFF_CHIP         <span class="o">=</span> <span class="mh">0x80000000</span><span class="p">,</span> <span class="c">///&lt; peak lands off edge of chip</span></td></tr><tr><th id="L39"><a href="#L39">39</a></th><td><span class="c"></span><span class="p">}</span> pmSourceMode<span class="p">;</span></td></tr><tr><th id="L40"><a href="#L40">40</a></th><td></td></tr><tr><th id="L41"><a href="#L41">41</a></th><td><span class="c">// Bit flags to distinguish analysis results</span></td></tr><tr><th id="L42"><a href="#L42">42</a></th><td><span class="c">// When adding to or subtracting from this list, please also modify pmSourceMaskHeader</span></td></tr><tr><th id="L43"><a href="#L43">43</a></th><td><span class="c"></span><span class="k">typedef</span> <span class="k">enum</span> <span class="p">{</span></td></tr><tr><th id="L44"><a href="#L44">44</a></th><td>    PM_SOURCE_MODE2_DEFAULT          <span class="o">=</span> <span class="mh">0x00000000</span><span class="p">,</span> <span class="c">///&lt; Initial value: resets all bits</span></td></tr><tr><th id="L45"><a href="#L45">45</a></th><td><span class="c"></span>    PM_SOURCE_MODE2_DIFF_WITH_SINGLE <span class="o">=</span> <span class="mh">0x00000001</span><span class="p">,</span> <span class="c">///&lt; diff source matched to a single positive detection</span></td></tr><tr><th id="L46"><a href="#L46">46</a></th><td><span class="c"></span>    PM_SOURCE_MODE2_DIFF_WITH_DOUBLE <span class="o">=</span> <span class="mh">0x00000002</span><span class="p">,</span> <span class="c">///&lt; diff source matched to positive detections in both images</span></td></tr><tr><th id="L47"><a href="#L47">47</a></th><td><span class="c"></span>    PM_SOURCE_MODE2_MATCHED          <span class="o">=</span> <span class="mh">0x00000004</span><span class="p">,</span> <span class="c">///&lt; diff source matched to positive detections in both images</span></td></tr><tr><th id="L48"><a href="#L48">48</a></th><td><span class="c"></span></td></tr><tr><th id="L49"><a href="#L49">49</a></th><td>    PM_SOURCE_MODE2_ON_SPIKE         <span class="o">=</span> <span class="mh">0x00000008</span><span class="p">,</span> <span class="c">///&lt; &gt; 25% of (PSF-weighted) pixels land on diffraction spike</span></td></tr><tr><th id="L50"><a href="#L50">50</a></th><td><span class="c"></span>    PM_SOURCE_MODE2_ON_STARCORE      <span class="o">=</span> <span class="mh">0x00000010</span><span class="p">,</span> <span class="c">///&lt; &gt; 25% of (PSF-weighted) pixels land on starcore</span></td></tr><tr><th id="L51"><a href="#L51">51</a></th><td><span class="c"></span>    PM_SOURCE_MODE2_ON_BURNTOOL      <span class="o">=</span> <span class="mh">0x00000020</span><span class="p">,</span> <span class="c">///&lt; &gt; 25% of (PSF-weighted) pixels land on burntool</span></td></tr><tr><th id="L52"><a href="#L52">52</a></th><td><span class="c"></span>    PM_SOURCE_MODE2_ON_CONVPOOR      <span class="o">=</span> <span class="mh">0x00000040</span><span class="p">,</span> <span class="c">///&lt; &gt; 25% of (PSF-weighted) pixels land on convpoor</span></td></tr><tr><th id="L53"><a href="#L53">53</a></th><td><span class="c"></span></td></tr><tr><th id="L54"><a href="#L54">54</a></th><td>    PM_SOURCE_MODE2_PASS1_SRC        <span class="o">=</span> <span class="mh">0x00000080</span><span class="p">,</span> <span class="c">///&lt; source detected in first pass analysis</span></td></tr><tr><th id="L55"><a href="#L55">55</a></th><td><span class="c"></span></td></tr><tr><th id="L56"><a href="#L56">56</a></th><td>    PM_SOURCE_MODE2_HAS_BRIGHTER_NEIGHBOR <span class="o">=</span> <span class="mh">0x00000100</span><span class="p">,</span> <span class="c">///&lt; peak is not the brightest in its footprint</span></td></tr><tr><th id="L57"><a href="#L57">57</a></th><td><span class="c"></span>    PM_SOURCE_MODE2_BRIGHT_NEIGHBOR_1     <span class="o">=</span> <span class="mh">0x00000200</span><span class="p">,</span> <span class="c">///&lt; flux_n / (r^2 flux_p) &gt; 1</span></td></tr><tr><th id="L58"><a href="#L58">58</a></th><td><span class="c"></span>    PM_SOURCE_MODE2_BRIGHT_NEIGHBOR_10    <span class="o">=</span> <span class="mh">0x00000400</span><span class="p">,</span> <span class="c">///&lt; flux_n / (r^2 flux_p) &gt; 10</span></td></tr><tr><th id="L59"><a href="#L59">59</a></th><td><span class="c"></span><span class="p">}</span> pmSourceMode2<span class="p">;</span></td></tr><tr><th id="L60"><a href="#L60">60</a></th><td></td></tr><tr><th id="L61"><a href="#L61">61</a></th><td><span class="c">/// Populate header with mask values</span></td></tr><tr><th id="L62"><a href="#L62">62</a></th><td><span class="c"></span>bool pmSourceMasksHeader<span class="p">(</span></td></tr><tr><th id="L63"><a href="#L63">63</a></th><td>    psMetadata <span class="o">*</span>header                  <span class="c">///&lt; Header to populate</span></td></tr><tr><th id="L64"><a href="#L64">64</a></th><td><span class="c"></span>    <span class="p">);</span></td></tr><tr><th id="L65"><a href="#L65">65</a></th><td><span class="cp"></span></td></tr><tr><th id="L66"><a href="#L66">66</a></th><td><span class="cp"></span></td></tr><tr><th id="L67"><a href="#L67">67</a></th><td><span class="cp"></span></td></tr><tr><th id="L68"><a href="#L68">68</a></th><td><span class="cp">#endif</span></td></tr></tbody></table>
                </div>
                <div id="help">
        <strong>Note:</strong> See <a href="/trac/ipp/wiki/TracBrowser">TracBrowser</a>
        for help on using the browser.
                </div>
                <div id="anydiff">
        <form action="/trac/ipp/diff" method="get">
                <div class="buttons">
            <input type="hidden" name="new_path" value="/trunk/psModules/src/objects/pmSourceMasks.h" />
            <input type="hidden" name="old_path" value="/trunk/psModules/src/objects/pmSourceMasks.h" />
            <input type="hidden" name="new_rev" value="31670" />
            <input type="hidden" name="old_rev" value="31670" />
            <input type="submit" value="View changes..." title="Select paths and revs for Diff" />
                </div>
        </form>
                </div>
                </div>
                <div id="altlinks">
      <h3>Download in other formats:</h3>
      <ul>
        <li class="first">
          <a rel="nofollow" href="/trac/ipp/browser/trunk/psModules/src/objects/pmSourceMasks.h?format=txt">Plain Text</a>
        </li><li class="last">
          <a rel="nofollow" href="/trac/ipp/export/32198/trunk/psModules/src/objects/pmSourceMasks.h">Original Format</a>
        </li>
      </ul>
                </div>
                </div>
                <div id="footer" lang="en" xml:lang="en">
                    <hr />
      <a id="tracpowered" href="http://trac.edgewall.org/"><img src="/trac/ipp/chrome/common/trac_logo_mini.png" height="30" width="107" alt="Trac Powered" /></a>
      <p class="left">
        Powered by <a href="/trac/ipp/about"><strong>Trac 0.11.2</strong></a>
        <br />
        By <a href="http://www.edgewall.org/">Edgewall Software</a>.
      </p>
      <p class="right">Visit the Trac open source project at<br /><a href="http://trac.edgewall.org/">http://trac.edgewall.org/</a></p>
                </div>
                </div>
        </body>
</html>