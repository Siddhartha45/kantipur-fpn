document.querySelector('.bd-navbar').innerHTML = 
`<nav class="navbar navbar-expand-lg">
<div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
        data-bs-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03"
        aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 flex-column db-navbar">

            <li class="nav-item">
                <a class="nav-link"
                    href="http://127.0.0.1:5500/html/">
                    <span class="material-symbols-outlined">
                        dashboard
                    </span> ड्यासबोर्ड</a>
            </li>

            <li class="nav-item">
                <a class="nav-link"
                    href="http://127.0.0.1:5500/html/namuna_bibaran/newentry.html"><span class="material-symbols-outlined">
                        summarize
                    </span>
                    खाद्य ऐन/नियम बमोजिम संकलित नमुना विवरण</a>
            </li>

            <li class="nav-item">
                <a class="nav-link"
                    href="http://127.0.0.1:5500/html/anugaman_bibaran/newentry.html"><span class="material-symbols-outlined">
                        summarize
                    </span>
                    निरीक्षण अनुगमन विवरण</a>
            </li>

            <li class="nav-item">
                <a class="nav-link"
                    href="http://127.0.0.1:5500/html/logobitaran_bibaran/newentry.html"><span class="material-symbols-outlined">
                        summarize
                    </span>
                    होटल स्तरीकरण लोगो वितरण सम्बन्धि विवरण</a>
            </li>
           
       

            <li class="nav-item">
            <a class="nav-link"
                href="http://127.0.0.1:5500/html/bisleysan_bibaran/newentry.html"><span class="material-symbols-outlined">
                    summarize
                </span>
                खाद्य तथा दाना नमुना विश्लेषण विवरण</a>
        </li>
        <li class="nav-item">
            <a class="nav-link"
                href="http://127.0.0.1:5500/html/pratibedan_bibaran/newentry.html"><span class="material-symbols-outlined">
                    summarize
                </span>
                प्रयोगशाला विश्लेषण प्रतिवेदन सारांश</a>
        </li>


            <li class="nav-item accordion" id="users">
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <p class="accordion-button collapsed" type="button"
                            data-bs-toggle="collapse" data-bs-target="#details-collapseregistration"
                            aria-expanded="false" aria-controls="details-collapseuser" style="line-height: 1.7;">
                            <span class="material-symbols-outlined">
                            new_window
                            </span>खाद्य तथा दाना अनुज्ञा पत्र जारी/नविकरण/उद्योग सिफारिस
                        </p>
                    </h2>
                    <div id="details-collapseregistration"
                        class="accordion-collapse details-collapseOne collapse">
                        <div class="accordion-body d-flex flex-column">
                            <a class="nav-link" href="http://127.0.0.1:5500/html/registration/new.html">खाद्य तथा दाना अनुज्ञा पत्र जारी</a>
                            <a class="nav-link" href="http://127.0.0.1:5500/html/registration/renew.html">खाद्य तथा दाना अनुज्ञा पत्र नविकरण</a>
                            <a class="nav-link" href="http://127.0.0.1:5500/html/registration/udyog.html">उद्योग सिफारिस</a>
                        </div>
                    </div>
                </div>
            </li>

            <li class="nav-item">
                <a class="nav-link"
                    href="http://127.0.0.1:5500/html/import-export/index.html"><span class="material-symbols-outlined">
                    flag
                    </span> आयात निर्यात गुण प्रमाणिकरण</a>
            </li>

            <li class="nav-item">
                <a class="nav-link"
                    href="http://127.0.0.1:5500/html/gunasho/index.html"><span class="material-symbols-outlined">
                    flag
                    </span> उजुरी/गुनासो ब्येवस्थापन</a>
            </li>

            <li class="nav-item">
                <a class="nav-link"
                    href="http://127.0.0.1:5500/html/hotel-patrakar/index.html"><span class="material-symbols-outlined">
                    event_list
                    </span>
                    खाद्य प्रसोधन, खाद्य पोषण, उद्योग, होटेल, पत्रकार, कार्यशाला आदि</a>
            </li>

            <li class="nav-item">
            <a class="nav-link"
                href="http://127.0.0.1:5500/html/account/summary.html"><span class="material-symbols-outlined">
                card_travel
                </span>
                मासिक वित्तिय विवरण</a>
            </li>

            <li class="nav-item">
                <a class="nav-link"
                    href="http://127.0.0.1:5500/html/report/summary.html"><span class="material-symbols-outlined">
                    summarize
                </span> 
                    मासिक प्रगति विवरण</a>
            </li>

            <li class="nav-item accordion" id="users">
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <p class="accordion-button collapsed" type="button"
                            data-bs-toggle="collapse" data-bs-target="#details-collapseuser"
                            aria-expanded="false" aria-controls="details-collapseuser">
                            <span class="material-symbols-outlined">
                                person</span>प्रयोगकर्ता
                        </p>
                    </h2>
                    <div id="details-collapseuser"
                        class="accordion-collapse details-collapseOne collapse">
                        <div class="accordion-body d-flex flex-column">
                            <a class="nav-link" href="http://127.0.0.1:5500/html/user/userdisplay.html">प्रयोगकर्ताहरु</a>
                            <a class="nav-link" href="http://127.0.0.1:5500/html/user/usercreate.html">प्रयोगकर्ता सृजना </a>
                        </div>
                    </div>
                </div>
            </li>

        </ul>
    </div>
</div>
</nav>`;


document.querySelector(".db-top-bar").innerHTML =
`<div class="db-lims-logo">
<a href="/">
    <div class="logo">
        <img src="../../image/np.png" alt="">
    </div>
</a>
<p>खाद्य प्रविधि तथा गुण <br>नियन्त्रण विभाग
</p>
</div>
<div class="db-top-bar-right">
<div class="db-user-profile">
    <div class="db-user-profile-right dropdown main">
        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown"
            aria-expanded="false">
            <div class="usersmimage-div">
                <img src="https://ui-avatars.com/api/?name=Pradeep+Marasini&rounded=true&background=FB802C&color=ffffff&size=28&bold=true"
                    alt="">
            </div>
            <div>
                <h3 class="username">Pradeep Marasini</h3>
                <p class="userrole">Super Admin</p>
            </div>
        </button>
        <ul class="dropdown-menu ">
            <li><a class="dropdown-item profile" href="http://127.0.0.1:5500/html/user/userprofile.html">My Account</a></li>
            <li>
                <a class="dropdown-item log-profile" href="">
                    Logout
                </a>
            </li>
        </ul>
    </div>
</div>
</div>`
