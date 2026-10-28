import os

index_content = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GARUDA QUANTUM 4D | Model Kuantitatif Multi-Aset Indonesia</title>
  <meta name="description" content="Model perdagangan kuantitatif multi-dimensi milik investor Indonesia. Metodologi 30 tahun IMF & Millennium Quant Pods untuk melindungi dan mengembangkan modal lintas siklus.">
  <link rel="icon" type="image/png" href="./assets/garuda_logo_hires.png">
  
  <!-- Open Graph Meta Tags -->
  <meta property="og:title" content="GARUDA QUANTUM 4D | Model Kuantitatif Multi-Aset Indonesia">
  <meta property="og:description" content="Metodologi alokasi kuantitatif 30 tahun IMF & Millennium Management untuk melindungi dan menumbuhkan modal investor Indonesia.">
  <meta property="og:type" content="website">
  <meta property="og:image" content="./assets/garuda_logo_hires.png">

  <!-- Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="./style.css">
</head>
<body>

  <!-- ========================================================
       ENTRANCE STAGE (ReactDrops-style Architectural Preloader)
       ======================================================== -->
  <main class="loading-stage">
    
    <!-- 1. Layer 1: Background & Construction View -->
    <div class="legacy-view" aria-hidden="true">
      
      <!-- Skip Entrance Animation Pill Button -->
      <button id="btn-skip-intro" class="skip-intro-btn" title="Lewati animasi pembuka" aria-label="Lewati Animasi">
        <span data-i18n="intro_skip">Lewati Animasi</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M5 12h14M12 5l7 7-7 7"/>
        </svg>
      </button>

      <div class="construction-container">
        <!-- Construction Grid Lines -->
        <div class="construction-line line-horizontal line-top"></div>
        <div class="construction-line line-horizontal line-bottom"></div>
        <div class="construction-line line-vertical line-left"></div>
        <div class="construction-line line-vertical line-right"></div>
        
        <div class="construction-line line-horizontal split-guide guide-inner-top"></div>
        <div class="construction-line line-horizontal split-guide guide-inner-bottom"></div>
        <div class="construction-line line-vertical split-guide guide-inner-left"></div>
        <div class="construction-line line-vertical split-guide guide-inner-right"></div>

        <!-- Center Seed Liquid Gradient Composition -->
        <div class="shared-gradient-composition">
          <div class="gradient-field"></div>
          <canvas class="noise-mask" width="128" height="128"></canvas>
          <div class="quad-tiles">
            <!-- D1: Equities SVG Icon -->
            <div class="quad-tile">
              <svg class="quad-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/>
                <polyline points="17 6 23 6 23 12"/>
              </svg>
              <span>D1</span>
            </div>
            <!-- D2: Fixed Income SVG Shield Icon -->
            <div class="quad-tile">
              <svg class="quad-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
              </svg>
              <span>D2</span>
            </div>
            <!-- D3: Commodities SVG Lightning Icon -->
            <div class="quad-tile">
              <svg class="quad-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
              </svg>
              <span>D3</span>
            </div>
            <!-- D4: Alternative SVG Atomic/Decentralized Icon -->
            <div class="quad-tile">
              <svg class="quad-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="3"/>
                <circle cx="19" cy="5" r="2"/>
                <circle cx="5" cy="19" r="2"/>
                <path d="M10.4 10.4 6.4 17.6M13.6 13.6l4-7.2M13.6 10.4l4 7.2M10.4 13.6l-4-7.2"/>
              </svg>
              <span>D4</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Wordmark Container positioned ABOVE the Four-Grid -->
      <div class="brand-wordmark-container">
        <div class="brand-emblem">
          <img src="./assets/garuda_logo_hires.png" alt="GARUDA QUANTUM" class="brand-emblem-img" width="56" height="56">
        </div>
        <div>
          <div class="brand-wordmark">GARUDA</div>
          <div class="brand-tagline-sub">QUANTUM 4D ARCHITECTURE</div>
        </div>
      </div>
    </div>

    <!-- 2. Layer 2: Backdrop Dark Scrim -->
    <div class="page-reveal-scrim" aria-hidden="true"></div>

    <!-- 3. Layer 3: THE MAIN SITE (Surface Entrance) -->
    <article class="page-reveal-surface" id="site-surface">

      <!-- Navigation Bar -->
      <header class="site-navbar">
        <a href="#" class="nav-brand" aria-label="Garuda Quantum 4D Home">
          <div class="nav-logo-icon">
            <img src="./assets/garuda_logo_hires.png" alt="GARUDA QUANTUM" class="nav-logo-img" width="36" height="36">
          </div>
          <div class="nav-brand-text">GARUDA <span>QUANTUM 4D</span></div>
        </a>

        <!-- Desktop Navigation Links -->
        <nav class="nav-links" aria-label="Main Navigation">
          <a href="#section-model" data-i18n="nav_model">Model 4D</a>
          <a href="#simulator-section" data-i18n="nav_sim">Simulator</a>
          <a href="#section-track" data-i18n="nav_track">Rekam Jejak</a>
          <a href="#section-compare" data-i18n="nav_compare">Keunggulan</a>
          <a href="#section-team" data-i18n="nav_team">Tim Riset</a>
          <a href="#section-pledge" data-i18n="nav_pledge">Komitmen 6.0</a>
        </nav>

        <div class="nav-actions">
          <!-- Institutional Language Switcher (Clean Text Pills) -->
          <div class="lang-switcher" role="group" aria-label="Language Selector">
            <button class="lang-btn active" data-lang="id" aria-pressed="true">ID</button>
            <button class="lang-btn" data-lang="en" aria-pressed="false">EN</button>
          </div>

          <!-- Community Access CTA -->
          <button class="btn-primary btn-nav-cta" id="btn-open-community-nav" data-i18n="nav_cta">Akses Riset</button>

          <!-- Mobile Hamburger Toggle Button -->
          <button class="mobile-toggle-btn" id="mobile-toggle" aria-label="Buka Menu Navigasi" aria-expanded="false">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </header>

      <!-- Mobile Navigation Drawer Dropdown -->
      <div class="mobile-nav-drawer" id="mobile-drawer" aria-hidden="true">
        <nav class="mobile-drawer-links">
          <a href="#section-model" class="mobile-nav-item" data-i18n="nav_model">Model 4D</a>
          <a href="#simulator-section" class="mobile-nav-item" data-i18n="nav_sim">Simulator</a>
          <a href="#section-track" class="mobile-nav-item" data-i18n="nav_track">Rekam Jejak</a>
          <a href="#section-compare" class="mobile-nav-item" data-i18n="nav_compare">Keunggulan</a>
          <a href="#section-team" class="mobile-nav-item" data-i18n="nav_team">Tim Riset</a>
          <a href="#section-pledge" class="mobile-nav-item" data-i18n="nav_pledge">Komitmen 6.0</a>
        </nav>
        <div class="mobile-drawer-footer">
          <div class="lang-switcher-mobile">
            <button class="lang-btn active" data-lang="id">Bahasa Indonesia</button>
            <button class="lang-btn" data-lang="en">English (UK)</button>
          </div>
          <button class="btn-primary w-full" id="btn-open-community-mobile" data-i18n="nav_cta">Akses Riset & Komunitas</button>
        </div>
      </div>

      <!-- ========================================================
           HERO SECTION (2-Column Institutional Terminal Layout)
           ======================================================== -->
      <section class="hero-section">
        <div class="hero-grid-container">
          
          <!-- Left Column: Value Proposition & High-Impact Typography -->
          <div class="hero-left-col">
            <div class="hero-badge-pill">
              <span class="hero-status-dot"></span>
              <span data-i18n="hero_badge">Model Kuantitatif Multi-Aset Milik Investor Indonesia</span>
            </div>

            <h1 class="hero-title">
              <span data-i18n="hero_title_1">Terbang Tinggi,</span><br>
              <span class="highlight-gold" data-i18n="hero_title_2">Melindungi Modal Anda</span>
            </h1>

            <p class="hero-description" data-i18n="hero_desc">
              Metodologi kuantitatif 30 tahun yang ditempa di IMF dan tim Systematic Quant Pods Millennium Management — kini dikalibrasi secara eksklusif untuk melindungi dan menumbuhkan kekayaan investor Indonesia di pasar global.
            </p>

            <div class="hero-cta-group">
              <a href="#section-model" class="btn-primary" data-i18n="hero_btn_explore">Eksplorasi Model 4D</a>
              <button class="btn-secondary" id="btn-hero-community" data-i18n="nav_cta">Akses Riset Institusional</button>
            </div>

            <!-- Key Quant Metrics Strip -->
            <div class="metrics-strip">
              <div class="metric-card reveal-on-scroll">
                <div class="metric-value gold" data-i18n="metric_1_val">4 Dimensi</div>
                <div class="metric-label" data-i18n="metric_1_lbl">Cakupan Ekuitas, Obligasi, Komoditas & Digital</div>
              </div>
              <div class="metric-card reveal-on-scroll">
                <div class="metric-value emerald" data-i18n="metric_2_val">+$130M</div>
                <div class="metric-label" data-i18n="metric_2_lbl">Profit Bersih Terverifikasi di 4 Krisis Black Swan</div>
              </div>
              <div class="metric-card reveal-on-scroll">
                <div class="metric-value" data-i18n="metric_3_val">2.45</div>
                <div class="metric-label" data-i18n="metric_3_lbl">Sharpe Ratio Teruji Lintas Siklus Makro Ekstrem</div>
              </div>
              <div class="metric-card reveal-on-scroll">
                <div class="metric-value" data-i18n="metric_4_val">100%</div>
                <div class="metric-label" data-i18n="metric_4_lbl">Sistematis Bebas Bias Emosi & Tebakan Ritel</div>
              </div>
            </div>
          </div>

          <!-- Right Column: Interactive 4D Terminal & Live Matrix Simulator -->
          <div class="hero-right-col" id="simulator-section">
            <div class="simulator-box">
              <div class="sim-header">
                <div class="sim-title">
                  <div class="sim-status-chip">
                    <span class="live-dot"></span>
                    <span data-i18n="sim_badge">TERMINAL LIVE CORRELATION</span>
                  </div>
                  <h3 data-i18n="sim_title">Simulator Korelasi Dinamis 4D</h3>
                  <p data-i18n="sim_sub">Uji bagaimana bobot alokasi sistem bergeser saat skenario makro ekstrem terdeteksi.</p>
                </div>
              </div>

              <!-- Interactive Scenario Selectors -->
              <div class="scenario-buttons" role="tablist" aria-label="Skenario Makro">
                <button class="scenario-btn active" data-scenario="normal" role="tab" aria-selected="true" data-i18n="sim_scen_normal">Pasar Berimbang</button>
                <button class="scenario-btn" data-scenario="inflation" role="tab" aria-selected="false" data-i18n="sim_scen_inflation">Inflasi & Rupiah Anjlok</button>
                <button class="scenario-btn" data-scenario="crash" role="tab" aria-selected="false" data-i18n="sim_scen_crash">Krisis Saham Global</button>
                <button class="scenario-btn" data-scenario="crypto" role="tab" aria-selected="false" data-i18n="sim_scen_crypto">Reli Siklus Kripto</button>
              </div>

              <!-- Dynamic 4D Weight Allocation Bars -->
              <div class="weight-bars-grid">
                <div class="weight-item">
                  <div class="weight-label">
                    <span class="weight-dim-name">
                      <svg class="dim-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>
                      <span data-i18n="sim_lbl_eq">Ekuitas</span>
                    </span>
                    <span class="weight-val-num" id="val-eq">35%</span>
                  </div>
                  <div class="bar-track"><div class="bar-fill eq-fill" id="fill-eq" style="width: 35%;"></div></div>
                </div>

                <div class="weight-item">
                  <div class="weight-label">
                    <span class="weight-dim-name">
                      <svg class="dim-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                      <span data-i18n="sim_lbl_fi">Obligasi</span>
                    </span>
                    <span class="weight-val-num" id="val-fi">30%</span>
                  </div>
                  <div class="bar-track"><div class="bar-fill fi-fill" id="fill-fi" style="width: 30%;"></div></div>
                </div>

                <div class="weight-item">
                  <div class="weight-label">
                    <span class="weight-dim-name">
                      <svg class="dim-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                      <span data-i18n="sim_lbl_com">Komoditas</span>
                    </span>
                    <span class="weight-val-num" id="val-com">20%</span>
                  </div>
                  <div class="bar-track"><div class="bar-fill com-fill" id="fill-com" style="width: 20%;"></div></div>
                </div>

                <div class="weight-item">
                  <div class="weight-label">
                    <span class="weight-dim-name">
                      <svg class="dim-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><circle cx="19" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><path d="M10.4 10.4 6.4 17.6M13.6 13.6l4-7.2"/></svg>
                      <span data-i18n="sim_lbl_alt">Aset Digital</span>
                    </span>
                    <span class="weight-val-num" id="val-alt">15%</span>
                  </div>
                  <div class="bar-track"><div class="bar-fill alt-fill" id="fill-alt" style="width: 15%;"></div></div>
                </div>
              </div>

              <!-- Real-time Macro Dynamic Strategy Explanation -->
              <div class="sim-explanation">
                <div class="sim-exp-badge">ANALISIS DINAMIS</div>
                <p id="sim-explanation-text">Kondisi pasar seimbang: Bobot terdistribusi proporsional untuk menangkap pertumbuhan tren IHSG/Global (35%), diimbangi cadangan obligasi stabil (30%) dan proteksi komoditas (20%).</p>
              </div>
            </div>
          </div>

        </div>
      </section>

      <!-- ========================================================
           SECTION 1: 4D CORE ARCHITECTURE & BENTO MATRIX
           ======================================================== -->
      <section class="section" id="section-model">
        <div class="section-header reveal-on-scroll">
          <span class="section-tag" data-i18n="s1_tag">Arsitektur Inti</span>
          <h2 class="section-title" data-i18n="s1_title">Mengapa GARUDA QUANTUM 4D Berbeda?</h2>
          <p class="section-subtitle" data-i18n="s1_sub">Bukan sekadar indikator saham atau robot trading pasaran, melainkan sistem alokasi multi-dimensi dengan proteksi korelasi dinamis.</p>
        </div>

        <!-- 4D Bento Matrix with Connected Visual Continuity -->
        <div class="bento-4d-grid">
          
          <!-- Dimension 1: Equities -->
          <div class="bento-dimension-card reveal-on-scroll">
            <div class="dim-card-header">
              <span class="dim-tag" data-i18n="dim_1_tag">Dimensi 1</span>
              <div class="dim-icon-wrapper">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>
              </div>
            </div>
            <h3 class="dim-title" data-i18n="dim_1_title">Ekuitas (Equities)</h3>
            <p class="dim-desc" data-i18n="dim_1_desc">Menangkap tren sekuler, rotasi sektoral IHSG, dan momentum saham teknologi global melalui pembobotan faktor risiko terukur.</p>
            <div class="dim-asset-list">
              <span class="dim-pill" data-i18n="dim_1_p1">IHSG & Big Caps</span>
              <span class="dim-pill" data-i18n="dim_1_p2">Global Tech</span>
              <span class="dim-pill" data-i18n="dim_1_p3">Momentum Faktor</span>
            </div>
          </div>

          <!-- Dimension 2: Fixed Income -->
          <div class="bento-dimension-card reveal-on-scroll">
            <div class="dim-card-header">
              <span class="dim-tag" data-i18n="dim_2_tag">Dimensi 2</span>
              <div class="dim-icon-wrapper">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
              </div>
            </div>
            <h3 class="dim-title" data-i18n="dim_2_title">Obligasi (Fixed Income)</h3>
            <p class="dim-desc" data-i18n="dim_2_desc">Menyediakan bantalan likuiditas institusional dan pertahanan siklis dari guncangan makro melalui durasi SBN dan US Treasuries.</p>
            <div class="dim-asset-list">
              <span class="dim-pill" data-i18n="dim_2_p1">Surat Berharga Negara (SBN)</span>
              <span class="dim-pill" data-i18n="dim_2_p2">US Treasuries</span>
              <span class="dim-pill" data-i18n="dim_2_p3">Buffer Likuiditas</span>
            </div>
          </div>

          <!-- Dimension 3: Commodities -->
          <div class="bento-dimension-card reveal-on-scroll">
            <div class="dim-card-header">
              <span class="dim-tag" data-i18n="dim_3_tag">Dimensi 3</span>
              <div class="dim-icon-wrapper">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
              </div>
            </div>
            <h3 class="dim-title" data-i18n="dim_3_title">Komoditas (Commodities)</h3>
            <p class="dim-desc" data-i18n="dim_3_desc">Benteng utama melawan lonjakan inflasi dan depresiasi mata uang Rupiah — memanfaatkan kekuatan riil sumber daya alam Indonesia.</p>
            <div class="dim-asset-list">
              <span class="dim-pill" data-i18n="dim_3_p1">Emas (XAU)</span>
              <span class="dim-pill" data-i18n="dim_3_p2">Nikel & Tembaga</span>
              <span class="dim-pill" data-i18n="dim_3_p3">Minyak & CPO</span>
            </div>
          </div>

          <!-- Dimension 4: Alternative Assets -->
          <div class="bento-dimension-card reveal-on-scroll">
            <div class="dim-card-header">
              <span class="dim-tag" data-i18n="dim_4_tag">Dimensi 4</span>
              <div class="dim-icon-wrapper">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><circle cx="19" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><path d="M10.4 10.4 6.4 17.6M13.6 13.6l4-7.2"/></svg>
              </div>
            </div>
            <h3 class="dim-title" data-i18n="dim_4_title">Aset Alternatif & Digital</h3>
            <p class="dim-desc" data-i18n="dim_4_desc">Menangkap imbal hasil non-linear dan volatilitas asimetris tinggi dengan parameter manajemen risiko drawdown yang sangat ketat.</p>
            <div class="dim-asset-list">
              <span class="dim-pill" data-i18n="dim_4_p1">Bitcoin & Top Crypto</span>
              <span class="dim-pill" data-i18n="dim_4_p2">Arbitrase Kerapuhan</span>
              <span class="dim-pill" data-i18n="dim_4_p3">Lindung Nilai Asimetris</span>
            </div>
          </div>

        </div>
      </section>

      <!-- ========================================================
           SECTION 2: VERIFIED BLACK SWAN TRACK RECORD TIMELINE
           ======================================================== -->
      <section class="section" id="section-track">
        <div class="section-header reveal-on-scroll">
          <span class="section-tag" data-i18n="s2_tag">Validasi Pasar Ekstrem</span>
          <h2 class="section-title" data-i18n="s2_title">Rekam Jejak Nyata di Tengah Badai Finansial</h2>
          <p class="section-subtitle" data-i18n="s2_sub">Strategi sejati tidak dinilai saat pasar sedang bull run, melainkan apakah modal Anda tetap utuh dan mencetak untung saat krisis melanda.</p>
        </div>

        <!-- Chronological Connected Timeline Track -->
        <div class="timeline-container">
          <div class="timeline-axis-line" aria-hidden="true"></div>

          <div class="timeline-track-grid">
            <!-- Event 1: 2008 Lehman -->
            <div class="track-record-card reveal-on-scroll">
              <div class="timeline-node-pin">2008</div>
              <span class="track-year-badge" data-i18n="track_1_year">Krisis Finansial Global 2008</span>
              <h3 class="track-title" data-i18n="track_1_title">Keruntuhan Lehman Brothers & Subprime CDO</h3>
              <p class="track-strategy" data-i18n="track_1_desc">Menurunkan eksposur aset risiko sebelum krisis, mengeksekusi posisi short terukur pada CDO subprime dan lembaga finansial bermasalah.</p>
              <div class="track-result-box">
                <span class="track-stat-label" data-i18n="track_1_stat_lbl">Pertumbuhan Modal Risiko</span>
                <span class="track-stat-num gold" data-i18n="track_1_stat_val">≥ 100% (+~$30M)</span>
              </div>
            </div>

            <!-- Event 2: 2021 May 19 -->
            <div class="track-record-card reveal-on-scroll">
              <div class="timeline-node-pin">2021</div>
              <span class="track-year-badge" data-i18n="track_2_year">Black Swan Kripto Mei 2021</span>
              <h3 class="track-title" data-i18n="track_2_title">Crash 5·19: Pengurasan Likuiditas Leverage</h3>
              <p class="track-strategy" data-i18n="track_2_desc">Mendeteksi kerapuhan likuiditas akibat tumpukan leverage derivatif, membatasi eksposur kripto &lt;5% dan membuka short hedging BTC/ETH.</p>
              <div class="track-result-box">
                <span class="track-stat-label" data-i18n="track_2_stat_lbl">Imbal Hasil Lindung Nilai</span>
                <span class="track-stat-num gold" data-i18n="track_2_stat_val">≥ 100% (+~$25M)</span>
              </div>
            </div>

            <!-- Event 3: 2022 LUNA -->
            <div class="track-record-card reveal-on-scroll">
              <div class="timeline-node-pin">2022</div>
              <span class="track-year-badge" data-i18n="track_3_year">Krisis Algoritmik 2022</span>
              <h3 class="track-title" data-i18n="track_3_title">Kejatuhan LUNA/UST Menuju Nol</h3>
              <p class="track-strategy" data-i18n="track_3_desc">Menganalisis cacat struktural pada mekanisme stabilitas algoritmik UST, mengeksekusi arbitrase dan posisi short saat terjadi depeg.</p>
              <div class="track-result-box">
                <span class="track-stat-label" data-i18n="track_3_stat_lbl">Keuntungan Bersih Arbitrase</span>
                <span class="track-stat-num emerald" data-i18n="track_3_stat_val">+$40M Profit</span>
              </div>
            </div>

            <!-- Event 4: 2022 FTX -->
            <div class="track-record-card reveal-on-scroll">
              <div class="timeline-node-pin">2022</div>
              <span class="track-year-badge" data-i18n="track_4_year">Krisis Kepercayaan 2022</span>
              <h3 class="track-title" data-i18n="track_4_title">Kebangkrutan Bursa FTX</h3>
              <p class="track-strategy" data-i18n="track_4_desc">Menarik aset sebelum insolvency terkonfirmasi ke publik, mengonfigurasi posisi short pada FTT dan token ekosistem terkait.</p>
              <div class="track-result-box">
                <span class="track-stat-label" data-i18n="track_4_stat_lbl">Proteksi & Posisi Short</span>
                <span class="track-stat-num emerald" data-i18n="track_4_stat_val">+$35M Profit</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================================
           SECTION 3: COMPARISON MATRIX TABLE
           ======================================================== -->
      <section class="section" id="section-compare">
        <div class="section-header reveal-on-scroll">
          <span class="section-tag" data-i18n="s3_tag">Transparansi Institusional</span>
          <h2 class="section-title" data-i18n="s3_title">GARUDA QUANTUM 4D vs Robot Trading Pasaran</h2>
          <p class="section-subtitle" data-i18n="s3_sub">Mengapa strategi kuantitatif sejati tidak dijual bebas di toko aplikasi? Memahami perbedaan antara rekayasa institusional dan skema pemasaran.</p>
        </div>

        <div class="table-container reveal-on-scroll">
          <table class="comparison-table">
            <thead>
              <tr>
                <th data-i18n="th_aspect">Dimensi Komparasi</th>
                <th class="col-public" data-i18n="th_public">Robot / Indikator Pasaran</th>
                <th class="col-garuda" data-i18n="th_garuda">GARUDA QUANTUM 4D</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="row-aspect" data-i18n="comp_row1_title">Asal Usul Strategi</td>
                <td class="col-public"><span class="table-cross">✕</span> <span data-i18n="comp_row1_pub">Salinan indikator umum (RSI/MACD) atau kemasan AI superficial</span></td>
                <td class="col-garuda"><span class="table-check">✓</span> <span data-i18n="comp_row1_garuda">Arsitektur orisinal riset 30 tahun (IMF & Millennium Quant Pods)</span></td>
              </tr>
              <tr>
                <td class="row-aspect" data-i18n="comp_row2_title">Metode Pengujian</td>
                <td class="col-public"><span class="table-cross">✕</span> <span data-i18n="comp_row2_pub">Hanya backtest historis statis yang mudah dimanipulasi</span></td>
                <td class="col-garuda"><span class="table-check">✓</span> <span data-i18n="comp_row2_garuda">Teruji di berbagai krisis Black Swan nyata dengan modal riil</span></td>
              </tr>
              <tr>
                <td class="row-aspect" data-i18n="comp_row3_title">Ketahanan Risiko</td>
                <td class="col-public"><span class="table-cross">✕</span> <span data-i18n="comp_row3_pub">Hanya bisa beli (long-only), rentan margin call saat market jatuh</span></td>
                <td class="col-garuda"><span class="table-check">✓</span> <span data-i18n="comp_row3_garuda">Mekanisme short-hedging bawaan, mampu mendulang profit di tren turun</span></td>
              </tr>
              <tr>
                <td class="row-aspect" data-i18n="comp_row4_title">Cakupan Aset</td>
                <td class="col-public"><span class="table-cross">✕</span> <span data-i18n="comp_row4_pub">Terbatas pada 1 instrumen (misal hanya emas atau hanya kripto)</span></td>
                <td class="col-garuda"><span class="table-check">✓</span> <span data-i18n="comp_row4_garuda">4 Dimensi dinamis (Saham, Obligasi, Komoditas, Aset Alternatif)</span></td>
              </tr>
              <tr>
                <td class="row-aspect" data-i18n="comp_row5_title">Eksklusivitas & Alfa</td>
                <td class="col-public"><span class="table-cross">✕</span> <span data-i18n="comp_row5_pub">Dijual massal ke publik (kehilangan efektivitas akibat arbitrase)</span></td>
                <td class="col-garuda"><span class="table-check">✓</span> <span data-i18n="comp_row5_garuda">Tertutup dan terbatas — melindungi alfa strategi agar tidak tergerus</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- ========================================================
           SECTION 4: LEADERSHIP & RESEARCH PROFILES
           ======================================================== -->
      <section class="section" id="section-team">
        <div class="section-header reveal-on-scroll">
          <span class="section-tag" data-i18n="s4_tag">Kepemimpinan & Tata Kelola</span>
          <h2 class="section-title" data-i18n="s4_title">Para Pengawal Modal Anda</h2>
          <p class="section-subtitle" data-i18n="s4_sub">Kombinasi pengalaman makro institusional puluhan tahun dengan keahlian kuantitatif dan kepemimpinan generasi baru.</p>
        </div>

        <div class="team-grid">
          <!-- Person 1: Jayendra Halim -->
          <div class="person-card reveal-on-scroll">
            <div class="person-photo-wrapper">
              <img src="./assets/jay_1.png" alt="Jayendra Halim" loading="lazy" width="600" height="800">
              <div class="photo-overlay"></div>
            </div>
            <div class="person-info">
              <h3 class="person-name">Jayendra Halim</h3>
              <div class="person-role" data-i18n="jay_role">Pendiri & Kepala Arsitek Kuantitatif</div>
              <p class="person-bio" data-i18n="jay_bio">
                Warga keturunan Indonesia generasi ketiga asal Bandung (64 tahun). Lebih dari 30 tahun berkarier di lembaga global: LSE, Oxford, Peneliti Senior di IMF (1990–1998), hingga memimpin Systematic Quant Pods di Millennium Management. Pengalaman selamat dari kebangkrutan pribadi di era dot-com 2000 membentuk filosofi disiplin risikonya yang tanpa kompromi.
              </p>
              <div class="person-credentials">
                <div class="credential-item">
                  <span class="cred-check">✓</span>
                  <div data-i18n="jay_cred1">Mantan Peneliti Senior Ekonomi International Monetary Fund (IMF)</div>
                </div>
                <div class="credential-item">
                  <span class="cred-check">✓</span>
                  <div data-i18n="jay_cred2">Mantan Kepala Riset Systematic Quant Pods — Millennium Management</div>
                </div>
                <div class="credential-item">
                  <span class="cred-check">✓</span>
                  <div data-i18n="jay_cred3">Arsitek Sistem GARUDA QUANTUM 4D (v1.0 hingga v6.0)</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Person 2: Aryana Widjaja -->
          <div class="person-card reveal-on-scroll">
            <div class="person-photo-wrapper">
              <img src="./assets/ayana_1.png" alt="Aryana Widjaja" loading="lazy" width="600" height="800">
              <div class="photo-overlay"></div>
            </div>
            <div class="person-info">
              <h3 class="person-name" data-i18n="ayana_name">Aryana Widjaja</h3>
              <div class="person-role" data-i18n="ayana_role">Kepala Riset Makro Asia-Pasifik & Risiko Digital</div>
              <p class="person-bio" data-i18n="ayana_bio">
                Alumni Jakarta Intercultural School (JIS), meraih gelar BBA Finance di National University of Singapore (NUS) dan MSc Finance di London School of Economics (LSE) dengan tesis 'Aplikasi AI dalam Manajemen Risiko Aset Digital', serta riset FinTech di Cambridge Judge Business School. Mengintegrasikan model AI kuantitatif modern dengan karakteristik pasar Indonesia.
              </p>
              <div class="person-credentials">
                <div class="credential-item">
                  <span class="cred-check">✓</span>
                  <div data-i18n="ayana_cred1">LSE MSc Finance & Riset FinTech Cambridge Judge Business School</div>
                </div>
                <div class="credential-item">
                  <span class="cred-check">✓</span>
                  <div data-i18n="ayana_cred2">Spesialis Manajemen Risiko Aset Digital & Analisis Kuantitatif AI</div>
                </div>
                <div class="credential-item">
                  <span class="cred-check">✓</span>
                  <div data-i18n="ayana_cred3">Kepala Pemantauan Risiko Lintas Aset Pasar Negara Berkembang</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================================
           SECTION 5: FOUNDER'S PLEDGE (SURAT TERBUKA & KOMITMEN)
           ======================================================== -->
      <section class="section" id="section-pledge">
        <div class="pledge-container reveal-on-scroll">
          <div class="pledge-content">
            <div class="pledge-badge" data-i18n="s5_badge">Surat Terbuka Jayendra Halim</div>
            <h2 class="pledge-title" data-i18n="s5_title">Mengapa Saya Kembali ke Indonesia, dan Mengapa Komitmen Ini Gratis</h2>
            
            <!-- Prominent Personal Quote Block -->
            <div class="pledge-quote-card">
              <p class="pledge-quote-text" data-i18n="hero_quote">“Pasar selalu memberi peluang baru, tetapi modal Anda tidak akan pernah memberi kesempatan kedua.”</p>
              <span class="pledge-quote-author" data-i18n="hero_quote_author">— Jayendra Halim, Pendiri & Kepala Arsitek Kuantitatif</span>
            </div>

            <div class="pledge-body">
              <p data-i18n="s5_p1">
                Saya lahir di Bandung. Tiga generasi keluarga saya berakar di tanah ini. Setelah tiga puluh tahun berjalan di pusat keuangan dunia dari London, Washington DC, hingga New York, setiap kali saya berdialog dengan investor di Jakarta, saya melihat kenyataan pahit: sebagian besar investor Indonesia masih berinvestasi dengan modal rumor, intuisi, dan tanpa perlindungan risiko yang memadai.
              </p>
              <p data-i18n="s5_p2">
                Jurang antara institusi Wall Street dan investor ritel Indonesia bukanlah pada kecerdasan atau modal, melainkan pada <strong>ketersediaan alat dan metodologi kuantitatif</strong>.
              </p>

              <div class="pledge-highlight-box">
                <h4 data-i18n="s5_box_title">Komitmen Transisi GARUDA QUANTUM v3.0 Menuju v6.0</h4>
                <p data-i18n="s5_box_desc">
                  GARUDA QUANTUM 4D saat ini berada pada Versi 3.0. Selama fase evolusi menuju Versi 6.0, model membutuhkan verifikasi data perilaku pasar nyata di Asia Tenggara. Ketika versi 6.0 selesai disempurnakan, saya berkomitmen memberikan akses model ini secara cuma-cuma kepada setiap anggota yang setia belajar dan berpraktik bersama kami.
                </p>
              </div>

              <p data-i18n="s5_p3">
                Ini bukan aksi amal sepihak, melainkan kemitraan sejati: Anda mendapatkan senjata kuantitatif institusional, model mendapatkan kalibrasi pasar nyata, dan kita bersama-sama membangun rekam jejak untuk peluncuran dana kelolaan swasta (Private Equity) masa depan Indonesia.
              </p>
            </div>

            <div class="pledge-signature">
              <div>
                <div class="sig-name">Jayendra Halim</div>
                <div class="sig-title" data-i18n="sig_title">Global Macro Scholar | Capital Steward</div>
              </div>
              <button class="btn-primary" id="btn-pledge-community" data-i18n="s5_cta">Bergabung dengan Komunitas Belajar</button>
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================================
           FOOTER (Institutional Governance, Office & Contact)
           ======================================================== -->
      <footer class="site-footer">
        <div class="footer-inner">
          <div class="footer-top">
            <div class="footer-brand">
              <div class="footer-brand-header">
                <img src="./assets/garuda_logo_hires.png" alt="GARUDA QUANTUM" class="footer-logo-img" width="30" height="30">
                <h4>GARUDA QUANTUM 4D</h4>
              </div>
              <p class="footer-entity-desc" data-i18n="foot_brand_desc">Sistem alokasi kuantitatif multi-dimensi eksklusif untuk pasar Indonesia. Dikembangkan oleh PT Garuda Kuantum Analitika.</p>
              <div class="footer-entity-meta">
                <span>Kantor Riset: SCBD Lot 28, Sudirman Central Business District, Jakarta Selatan</span>
                <span>Email: <a href="mailto:research@garudaquantum.id">research@garudaquantum.id</a></span>
              </div>
            </div>

            <!-- Official Community & Fast Channel Links -->
            <div class="footer-links-col">
              <h5 class="footer-col-title">Saluran Resmi</h5>
              <ul class="footer-links-list">
                <li><a href="https://wa.me/?text=Halo%20Garuda%20Quantum%20Desk" target="_blank" rel="noopener noreferrer">WhatsApp VIP Desk</a></li>
                <li><a href="https://t.me/GarudaQuantum4D" target="_blank" rel="noopener noreferrer">Telegram Channel Riset</a></li>
                <li><button class="footer-action-link" id="btn-footer-waitlist">Waitlist Private Equity</button></li>
                <li>
                  <button class="footer-action-link replay-footer-btn" id="btn-replay-intro">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/>
                    </svg>
                    <span data-i18n="nav_replay">Putar Ulang Animasi</span>
                  </button>
                </li>
              </ul>
            </div>
          </div>
          
          <div class="footer-disclaimer">
            <p data-i18n="foot_disclaimer">
              Pemberitahuan Risiko: Kinerja masa lalu tidak menjamin hasil masa depan. GARUDA QUANTUM 4D dirancang untuk tujuan analisis risiko kuantitatif dan edukasi manajemen modal. Pastikan Anda memahami profil risiko dan mengelola likuiditas modal Anda dengan bijak.
            </p>
            <p class="foot-copy-row">
              <span data-i18n="foot_copy">© 2026 GARUDA QUANTUM 4D. Hak Cipta Dilindungi Undang-Undang.</span>
              <span class="foot-slogan-text" data-i18n="foot_slogan">Terbang Tinggi, Melindungi Modal Anda</span>
            </p>
          </div>
        </div>
      </footer>

    </article>
  </main>

  <!-- ========================================================
       COMMUNITY & INSTITUTIONAL ACCESS MODAL
       ======================================================== -->
  <div class="community-modal-backdrop" id="community-modal" aria-hidden="true">
    <div class="community-modal-card" role="dialog" aria-modal="true" aria-labelledby="modal-title">
      <button class="modal-close-btn" id="modal-close-btn" aria-label="Tutup Jendela Modal">✕</button>
      
      <div class="modal-badge-chip">AKSES INSTITUSIONAL</div>
      <h3 class="modal-title" id="modal-title" data-i18n="modal_title">Bergabung dengan Komunitas Riset GARUDA QUANTUM</h3>
      <p class="modal-desc" data-i18n="modal_desc">Dapatkan akses langsung ke kalibrasi model harian, sinyal proteksi korelasi makro, dan ruang diskusi langsung bersama tim riset kuantitatif.</p>

      <div class="modal-channels-grid">
        <a href="https://wa.me/?text=Halo%20Tim%20Riset%20Garuda%20Quantum%204D" target="_blank" rel="noopener noreferrer" class="channel-card whatsapp-channel">
          <div class="channel-icon-circle">
            <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
          </div>
          <div class="channel-info">
            <span class="channel-name">WhatsApp VIP Desk</span>
            <span class="channel-sub">Hubungi langsung representatif riset privat</span>
          </div>
          <span class="channel-arrow">→</span>
        </a>

        <a href="https://t.me/GarudaQuantum4D" target="_blank" rel="noopener noreferrer" class="channel-card telegram-channel">
          <div class="channel-icon-circle">
            <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor"><path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm5.894 8.221l-1.97 9.28c-.145.658-.537.818-1.084.508l-3-2.21-1.446 1.394c-.16.16-.295.295-.605.295l.213-3.053 5.56-5.023c.242-.213-.054-.333-.373-.121l-6.871 4.326-2.962-.924c-.643-.204-.657-.643.136-.953l11.57-4.461c.536-.194 1.006.131.832.942z"/></svg>
          </div>
          <div class="channel-info">
            <span class="channel-name">Telegram Alpha Broadcast</span>
            <span class="channel-sub">Pembaruan indikator korelasi & laporan makro harian</span>
          </div>
          <span class="channel-arrow">→</span>
        </a>
      </div>

      <!-- Quick Waitlist Form -->
      <form class="modal-waitlist-form" id="waitlist-form">
        <label class="form-label" for="wl-email" data-i18n="modal_email_label">Daftar Minat Private Equity Fund & Riset v6.0</label>
        <div class="form-input-group">
          <input type="email" id="wl-email" class="form-input" placeholder="Masukkan alamat email Anda" required>
          <button type="submit" class="btn-primary" data-i18n="modal_btn_submit">Daftar</button>
        </div>
        <div class="form-success-msg" id="form-success-msg" style="display:none;" data-i18n="modal_success">✓ Terima kasih. Tim riset akan segera mengirimkan konfirmasi undangan.</div>
      </form>
    </div>
  </div>

  <!-- GSAP Local & Instant CDN Fallback -->
  <script src="./gsap.min.js"></script>
  <script>
    // Fail-safe protection: If GSAP fails to load or takes > 2.5s, automatically unlock site
    setTimeout(function() {
      if (!window.gsap || !document.querySelector('.page-reveal-surface.hero-revealed')) {
        document.documentElement.classList.add('no-gsap');
        var s = document.querySelector('.page-reveal-surface');
        if (s) {
          s.classList.add('hero-revealed');
        }
      }
    }, 2500);
  </script>

  <!-- Main Interactive Engine Script -->
  <script src="./app.js"></script>
</body>
</html>
"""

with open(r'c:\Users\Administrator\Desktop\新建文件夹 (5)\index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Updated index.html successfully!")
