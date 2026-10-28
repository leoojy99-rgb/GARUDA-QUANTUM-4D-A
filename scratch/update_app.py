app_content = """/**
 * GARUDA QUANTUM 4D - Official Web Application Engine
 * Optimized for High Performance, Zero-Bug Resilience, and Institutional Polish
 */

// ==========================================
// 1. COMPREHENSIVE BILINGUAL DICTIONARY (ID & EN)
// ==========================================
const translations = {
  id: {
    // Meta & Head
    site_title: "GARUDA QUANTUM 4D | Model Kuantitatif Multi-Aset Indonesia",
    site_desc: "Model perdagangan kuantitatif 30 tahun yang ditempa di IMF & Millennium Management Systematic Quant Pods untuk melindungi dan menumbuhkan modal investor Indonesia.",
    intro_skip: "Lewati Animasi",

    // Navigation
    nav_model: "Model 4D",
    nav_sim: "Simulator",
    nav_track: "Rekam Jejak",
    nav_compare: "Keunggulan",
    nav_team: "Tim Riset",
    nav_pledge: "Komitmen 6.0",
    nav_cta: "Akses Riset",
    nav_replay: "Putar Ulang Animasi",

    // Hero Section
    hero_badge: "Model Kuantitatif Multi-Aset Milik Investor Indonesia",
    hero_title_1: "Terbang Tinggi,",
    hero_title_2: "Melindungi Modal Anda",
    hero_quote: "“Pasar selalu memberi peluang baru, tetapi modal Anda tidak akan pernah memberi kesempatan kedua.”",
    hero_quote_author: "— Jayendra Halim, Pendiri & Kepala Arsitek Kuantitatif",
    hero_desc: "Metodologi kuantitatif 30 tahun yang ditempa di IMF dan tim Systematic Quant Pods Millennium Management — kini dikalibrasi secara eksklusif untuk melindungi dan menumbuhkan kekayaan investor Indonesia di pasar global.",
    hero_btn_explore: "Eksplorasi Model 4D",

    // Metrics Strip
    metric_1_val: "4 Dimensi",
    metric_1_lbl: "Cakupan Ekuitas, Obligasi, Komoditas & Digital",
    metric_2_val: "+$130M",
    metric_2_lbl: "Profit Bersih Terverifikasi di 4 Krisis Black Swan",
    metric_3_val: "2.45",
    metric_3_lbl: "Sharpe Ratio Teruji Lintas Siklus Makro Ekstrem",
    metric_4_val: "100%",
    metric_4_lbl: "Sistematis Bebas Bias Emosi & Tebakan Ritel",

    // Terminal Simulator
    sim_badge: "TERMINAL LIVE CORRELATION",
    sim_title: "Simulator Korelasi Dinamis 4D",
    sim_sub: "Uji bagaimana bobot alokasi sistem bergeser saat skenario makro ekstrem terdeteksi.",
    sim_scen_normal: "Pasar Berimbang",
    sim_scen_inflation: "Inflasi & Rupiah Anjlok",
    sim_scen_crash: "Krisis Saham Global",
    sim_scen_crypto: "Reli Siklus Kripto",
    sim_lbl_eq: "Ekuitas",
    sim_lbl_fi: "Obligasi",
    sim_lbl_com: "Komoditas",
    sim_lbl_alt: "Aset Digital",

    // Section 1: 4D Architecture
    s1_tag: "Arsitektur Inti",
    s1_title: "Mengapa GARUDA QUANTUM 4D Berbeda?",
    s1_sub: "Bukan sekadar indikator saham atau robot trading pasaran, melainkan sistem alokasi multi-dimensi dengan proteksi korelasi dinamis.",
    
    dim_1_tag: "Dimensi 1",
    dim_1_title: "Ekuitas (Equities)",
    dim_1_desc: "Menangkap tren sekuler, rotasi sektoral IHSG, dan momentum saham teknologi global melalui pembobotan faktor risiko terukur.",
    dim_1_p1: "IHSG & Big Caps", dim_1_p2: "Global Tech", dim_1_p3: "Momentum Faktor",

    dim_2_tag: "Dimensi 2",
    dim_2_title: "Obligasi (Fixed Income)",
    dim_2_desc: "Menyediakan bantalan likuiditas institusional dan pertahanan siklis dari guncangan makro melalui durasi SBN dan US Treasuries.",
    dim_2_p1: "Surat Berharga Negara (SBN)", dim_2_p2: "US Treasuries", dim_2_p3: "Buffer Likuiditas",

    dim_3_tag: "Dimensi 3",
    dim_3_title: "Komoditas (Commodities)",
    dim_3_desc: "Benteng utama melawan lonjakan inflasi dan depresiasi mata uang Rupiah — memanfaatkan kekuatan riil sumber daya alam Indonesia.",
    dim_3_p1: "Emas (XAU)", dim_3_p2: "Nikel & Tembaga", dim_3_p3: "Minyak & CPO",

    dim_4_tag: "Dimensi 4",
    dim_4_title: "Aset Alternatif & Digital",
    dim_4_desc: "Menangkap imbal hasil non-linear dan volatilitas asimetris tinggi dengan parameter manajemen risiko drawdown yang sangat ketat.",
    dim_4_p1: "Bitcoin & Top Crypto", dim_4_p2: "Arbitrase Kerapuhan", dim_4_p3: "Lindung Nilai Asimetris",

    // Section 2: Black Swan Timeline
    s2_tag: "Validasi Pasar Ekstrem",
    s2_title: "Rekam Jejak Nyata di Tengah Badai Finansial",
    s2_sub: "Strategi sejati tidak dinilai saat pasar sedang bull run, melainkan apakah modal Anda tetap utuh dan mencetak untung saat krisis melanda.",

    track_1_year: "Krisis Finansial Global 2008",
    track_1_title: "Keruntuhan Lehman Brothers & Subprime CDO",
    track_1_desc: "Menurunkan eksposur aset risiko sebelum krisis, mengeksekusi posisi short terukur pada CDO subprime dan lembaga finansial bermasalah.",
    track_1_stat_lbl: "Pertumbuhan Modal Risiko",
    track_1_stat_val: "≥ 100% (+~$30M)",

    track_2_year: "Black Swan Kripto Mei 2021",
    track_2_title: "Crash 5·19: Pengurasan Likuiditas Leverage",
    track_2_desc: "Mendeteksi kerapuhan likuiditas akibat tumpukan leverage derivatif, membatasi eksposur kripto <5% dan membuka short hedging BTC/ETH.",
    track_2_stat_lbl: "Imbal Hasil Lindung Nilai",
    track_2_stat_val: "≥ 100% (+~$25M)",

    track_3_year: "Krisis Algoritmik 2022",
    track_3_title: "Kejatuhan LUNA/UST Menuju Nol",
    track_3_desc: "Menganalisis cacat struktural pada mekanisme stabilitas algoritmik UST, mengeksekusi arbitrase dan posisi short saat terjadi depeg.",
    track_3_stat_lbl: "Keuntungan Bersih Arbitrase",
    track_3_stat_val: "+$40M Profit",

    track_4_year: "Krisis Kepercayaan 2022",
    track_4_title: "Kebangkrutan Bursa FTX",
    track_4_desc: "Menarik aset sebelum insolvency terkonfirmasi ke publik, mengonfigurasi posisi short pada FTT dan token ekosistem terkait.",
    track_4_stat_lbl: "Proteksi & Posisi Short",
    track_4_stat_val: "+$35M Profit",

    // Section 3: Comparison
    s3_tag: "Transparansi Institusional",
    s3_title: "GARUDA QUANTUM 4D vs Robot Trading Pasaran",
    s3_sub: "Mengapa strategi kuantitatif sejati tidak dijual bebas di toko aplikasi? Memahami perbedaan antara rekayasa institusional dan skema pemasaran.",
    th_aspect: "Dimensi Komparasi",
    th_public: "Robot / Indikator Pasaran",
    th_garuda: "GARUDA QUANTUM 4D",

    comp_row1_title: "Asal Usul Strategi",
    comp_row1_pub: "Salinan indikator umum (RSI/MACD) atau kemasan AI superficial",
    comp_row1_garuda: "Arsitektur orisinal riset 30 tahun (IMF & Millennium Quant Pods)",

    comp_row2_title: "Metode Pengujian",
    comp_row2_pub: "Hanya backtest historis statis yang mudah dimanipulasi",
    comp_row2_garuda: "Teruji di berbagai krisis Black Swan nyata dengan modal riil",

    comp_row3_title: "Ketahanan Risiko",
    comp_row3_pub: "Hanya bisa beli (long-only), rentan margin call saat market jatuh",
    comp_row3_garuda: "Mekanisme short-hedging bawaan, mampu mendulang profit di tren turun",

    comp_row4_title: "Cakupan Aset",
    comp_row4_pub: "Terbatas pada 1 instrumen (misal hanya emas atau hanya kripto)",
    comp_row4_garuda: "4 Dimensi dinamis (Saham, Obligasi, Komoditas, Aset Alternatif)",

    comp_row5_title: "Eksklusivitas & Alfa",
    comp_row5_pub: "Dijual massal ke publik (kehilangan efektivitas akibat arbitrase)",
    comp_row5_garuda: "Tertutup dan terbatas — melindungi alfa strategi agar tidak tergerus",

    // Section 4: Leadership
    s4_tag: "Kepemimpinan & Tata Kelola",
    s4_title: "Para Pengawal Modal Anda",
    s4_sub: "Kombinasi pengalaman makro institusional puluhan tahun dengan keahlian kuantitatif dan kepemimpinan generasi baru.",

    jay_role: "Pendiri & Kepala Arsitek Kuantitatif",
    jay_bio: "Warga keturunan Indonesia generasi ketiga asal Bandung (64 tahun). Lebih dari 30 tahun berkarier di lembaga global: LSE, Oxford, Peneliti Senior di IMF (1990–1998), hingga memimpin Systematic Quant Pods di Millennium Management. Pengalaman selamat dari kebangkrutan pribadi di era dot-com 2000 membentuk filosofi disiplin risikonya yang tanpa kompromi.",
    jay_cred1: "Mantan Peneliti Senior Ekonomi International Monetary Fund (IMF)",
    jay_cred2: "Mantan Kepala Riset Systematic Quant Pods — Millennium Management",
    jay_cred3: "Arsitek Sistem GARUDA QUANTUM 4D (v1.0 hingga v6.0)",

    ayana_name: "Aryana Widjaja",
    ayana_role: "Kepala Riset Makro Asia-Pasifik & Risiko Digital",
    ayana_bio: "Alumni Jakarta Intercultural School (JIS), meraih gelar BBA Finance di National University of Singapore (NUS) dan MSc Finance di London School of Economics (LSE) dengan tesis 'Aplikasi AI dalam Manajemen Risiko Aset Digital', serta riset FinTech di Cambridge Judge Business School. Mengintegrasikan model AI kuantitatif modern dengan karakteristik pasar Indonesia.",
    ayana_cred1: "LSE MSc Finance & Riset FinTech Cambridge Judge Business School",
    ayana_cred2: "Spesialis Manajemen Risiko Aset Digital & Analisis Kuantitatif AI",
    ayana_cred3: "Kepala Pemantauan Risiko Lintas Aset Pasar Negara Berkembang",

    // Section 5: Pledge (Surat Terbuka)
    s5_badge: "Surat Terbuka Jayendra Halim",
    s5_title: "Mengapa Saya Kembali ke Indonesia, dan Mengapa Komitmen Ini Gratis",
    s5_p1: "Saya lahir di Bandung. Tiga generasi keluarga saya berakar di tanah ini. Setelah tiga puluh tahun berjalan di pusat keuangan dunia dari London, Washington DC, hingga New York, setiap kali saya berdialog dengan investor di Jakarta, saya melihat kenyataan pahit: sebagian besar investor Indonesia masih berinvestasi dengan modal rumor, intuisi, dan tanpa perlindungan risiko yang memadai.",
    s5_p2: "Jurang antara institusi Wall Street dan investor ritel Indonesia bukanlah pada kecerdasan atau modal, melainkan pada <strong>ketersediaan alat dan metodologi kuantitatif</strong>.",
    s5_box_title: "Komitmen Transisi GARUDA QUANTUM v3.0 Menuju v6.0",
    s5_box_desc: "GARUDA QUANTUM 4D saat ini berada pada Versi 3.0. Selama fase evolusi menuju Versi 6.0, model membutuhkan verifikasi data perilaku pasar nyata di Asia Tenggara. Ketika versi 6.0 selesai disempurnakan, saya berkomitmen memberikan akses model ini secara cuma-cuma kepada setiap anggota yang setia belajar dan berpraktik bersama kami.",
    s5_p3: "Ini bukan aksi amal sepihak, melainkan kemitraan sejati: Anda mendapatkan senjata kuantitatif institusional, model mendapatkan kalibrasi pasar nyata, dan kita bersama-sama membangun rekam jejak untuk peluncuran dana kelolaan swasta (Private Equity) masa depan Indonesia.",
    s5_cta: "Bergabung dengan Komunitas Belajar",
    sig_title: "Global Macro Scholar | Capital Steward",

    // Footer
    foot_brand_desc: "Sistem alokasi kuantitatif multi-dimensi eksklusif untuk pasar Indonesia. Dikembangkan oleh PT Garuda Kuantum Analitika.",
    foot_disclaimer: "Pemberitahuan Risiko: Kinerja masa lalu tidak menjamin hasil masa depan. GARUDA QUANTUM 4D dirancang untuk tujuan analisis risiko kuantitatif dan edukasi manajemen modal. Pastikan Anda memahami profil risiko dan mengelola likuiditas modal Anda dengan bijak.",
    foot_copy: "© 2026 GARUDA QUANTUM 4D. Hak Cipta Dilindungi Undang-Undang.",
    foot_slogan: "Terbang Tinggi, Melindungi Modal Anda",

    // Community Modal
    modal_title: "Bergabung dengan Komunitas Riset GARUDA QUANTUM",
    modal_desc: "Dapatkan akses langsung ke kalibrasi model harian, sinyal proteksi korelasi makro, dan ruang diskusi langsung bersama tim riset kuantitatif.",
    modal_email_label: "Daftar Minat Private Equity Fund & Riset v6.0",
    modal_btn_submit: "Daftar",
    modal_success: "✓ Terima kasih. Tim riset akan segera mengirimkan konfirmasi undangan."
  },

  en: {
    // Meta & Head
    site_title: "GARUDA QUANTUM 4D | Institutional Multi-Asset Quant Engine",
    site_desc: "30-year systematic quantitative methodology forged across the IMF and Millennium Management Systematic Quant Pods — calibrated exclusively to protect and grow investor capital.",
    intro_skip: "Skip Intro",

    // Navigation
    nav_model: "4D Model",
    nav_sim: "Simulator",
    nav_track: "Track Record",
    nav_compare: "The Edge",
    nav_team: "Research Team",
    nav_pledge: "Pledge 6.0",
    nav_cta: "Research Access",
    nav_replay: "Replay Intro",

    // Hero Section
    hero_badge: "Indonesia's Proprietary Multi-Asset Quantitative Engine",
    hero_title_1: "Soar High,",
    hero_title_2: "Safeguard Your Capital",
    hero_quote: "“The market always offers fresh opportunities, but your capital will never grant you a second chance.”",
    hero_quote_author: "— Jayendra Halim, Founder & Principal Quant Architect",
    hero_desc: "Three decades of systematic quantitative methodology forged across the IMF and Millennium Management's Systematic Quant Pods — now calibrated exclusively to protect and compound the wealth of Indonesian investors in global markets.",
    hero_btn_explore: "Explore 4D Model",

    // Metrics Strip
    metric_1_val: "4 Dimensions",
    metric_1_lbl: "Equities, Fixed Income, Commodities & Digital Assets",
    metric_2_val: "+$130M",
    metric_2_lbl: "Verified Net Profit Across 4 Historic Black Swans",
    metric_3_val: "2.45",
    metric_3_lbl: "All-Weather Sharpe Ratio Tested Across Severe Regimes",
    metric_4_val: "100%",
    metric_4_lbl: "Systematic Quantitative Rules — Zero Emotional Bias",

    // Terminal Simulator
    sim_badge: "LIVE CORRELATION TERMINAL",
    sim_title: "4D Dynamic Correlation Simulator",
    sim_sub: "Test how the system's dynamic asset weights automatically shift under extreme macroeconomic stress.",
    sim_scen_normal: "Balanced Market",
    sim_scen_inflation: "Inflation & FX Shock",
    sim_scen_crash: "Global Equity Crash",
    sim_scen_crypto: "Crypto Cycle Rally",
    sim_lbl_eq: "Equities",
    sim_lbl_fi: "Fixed Income",
    sim_lbl_com: "Commodities",
    sim_lbl_alt: "Digital Assets",

    // Section 1: 4D Architecture
    s1_tag: "Core Architecture",
    s1_title: "Why GARUDA QUANTUM 4D Stands Apart",
    s1_sub: "Not an ordinary stock indicator or commercial trading bot, but a multi-dimensional allocation engine with dynamic cross-correlation defense.",

    dim_1_tag: "Dimension 1",
    dim_1_title: "Equities",
    dim_1_desc: "Capturing secular trends, IDX sector rotations, and global technology momentum through measured risk-factor weightings.",
    dim_1_p1: "IDX & Global Big Caps", dim_1_p2: "Global Tech", dim_1_p3: "Factor Momentum",

    dim_2_tag: "Dimension 2",
    dim_2_title: "Fixed Income",
    dim_2_desc: "Providing institutional liquidity buffers and cyclical protection against macro shocks via SBN duration and US Treasuries.",
    dim_2_p1: "SBN Sovereign Bonds", dim_2_p2: "US Treasuries", dim_2_p3: "Liquidity Buffer",

    dim_3_tag: "Dimension 3",
    dim_3_title: "Commodities",
    dim_3_desc: "Primary fortress against inflation surges and Rupiah depreciation — harnessing Indonesia's tangible natural resource strengths.",
    dim_3_p1: "Gold (XAU)", dim_3_p2: "Nickel & Copper", dim_3_p3: "Crude Oil & CPO",

    dim_4_tag: "Dimension 4",
    dim_4_title: "Alternative & Digital Assets",
    dim_4_desc: "Capturing non-linear returns and asymmetric upside with strict drawdown risk parameters and dynamic volatility throttling.",
    dim_4_p1: "Bitcoin & Top Assets", dim_4_p2: "Fragility Arbitrage", dim_4_p3: "Asymmetric Hedging",

    // Section 2: Black Swan Timeline
    s2_tag: "Extreme Market Validation",
    s2_title: "Proven Track Record in Financial Storms",
    s2_sub: "True institutional strategies are not measured during effortless bull markets, but by whether your capital remains intact and profitable when crisis strikes.",

    track_1_year: "Global Financial Crisis 2008",
    track_1_title: "Lehman Brothers & Subprime CDO Collapse",
    track_1_desc: "Pre-emptively de-risked beta exposure, deploying measured short positions on distressed mortgage pools and vulnerable financial institutions.",
    track_1_stat_lbl: "Risk Capital Growth",
    track_1_stat_val: "≥ 100% (+~$30M)",

    track_2_year: "Crypto Black Swan May 2021",
    track_2_title: "5·19 Crash: Leverage Liquidation Cascade",
    track_2_desc: "Detected acute structural fragility in derivative open interest, capping exposure <5% while executing decisive short-hedges on BTC/ETH.",
    track_2_stat_lbl: "Hedging Net Return",
    track_2_stat_val: "≥ 100% (+~$25M)",

    track_3_year: "Algorithmic Crisis 2022",
    track_3_title: "LUNA/UST Collapse to Zero",
    track_3_desc: "Diagnosed fundamental design flaws in algorithmic stability mechanics, capturing direct arbitrage and aggressive downside delta during depegging.",
    track_3_stat_lbl: "Arbitrage Net Gain",
    track_3_stat_val: "+$40M Profit",

    track_4_year: "Counterparty Crisis 2022",
    track_4_title: "FTX Exchange Insolvency",
    track_4_desc: "Evacuated exchange assets prior to public confirmation of insolvency, establishing tactical shorts against ecosystem tokens.",
    track_4_stat_lbl: "Hedging & Capital Defense",
    track_4_stat_val: "+$35M Profit",

    // Section 3: Comparison
    s3_tag: "Institutional Transparency",
    s3_title: "GARUDA QUANTUM 4D vs Public Trading Bots",
    s3_sub: "Why genuine institutional quantitative systems are never sold in app stores: understanding the divide between institutional engineering and retail marketing.",
    th_aspect: "Comparison Aspect",
    th_public: "Retail Bots / Public Indicators",
    th_garuda: "GARUDA QUANTUM 4D",

    comp_row1_title: "Strategy Provenance",
    comp_row1_pub: "Generic repackaged indicators (RSI/MACD) or superficial AI wrappers",
    comp_row1_garuda: "Original 30-year research pedigree (IMF & Millennium Quant Pods)",

    comp_row2_title: "Validation Methodology",
    comp_row2_pub: "Static historical backtests easily prone to curve-fitting",
    comp_row2_garuda: "Stress-tested across genuine historic Black Swan crises with real capital",

    comp_row3_title: "Downside Robustness",
    comp_row3_pub: "Long-only bias vulnerable to catastrophic drawdowns and margin calls",
    comp_row3_garuda: "Native short-hedging engine capable of generating alpha in sharp downtrends",

    comp_row4_title: "Asset Breadth",
    comp_row4_pub: "Confined to 1 isolated instrument (e.g. only Gold or only crypto)",
    comp_row4_garuda: "4 Dynamic dimensions (Equities, Fixed Income, Commodities, Digital)",

    comp_row5_title: "Exclusivity & Alpha Decay",
    comp_row5_pub: "Mass-marketed to retail, quickly eroding any statistical edge via crowding",
    comp_row5_garuda: "Private and capacity-constrained — protecting strategy alpha from decay",

    // Section 4: Leadership
    s4_tag: "Leadership & Research Governance",
    s4_title: "The Stewards of Your Capital",
    s4_sub: "Blending decades of institutional global macro experience with modern computational quantitative research.",

    jay_role: "Founder & Principal Quant Architect",
    jay_bio: "Third-generation Indonesian heritage from Bandung (64 years old). Over 30 years across global financial institutions: LSE, Oxford, Senior Researcher at the IMF (1990–1998), and leader of Systematic Quant Pods at Millennium Management. Surviving personal insolvency during the 2000 dot-com crash forged his uncompromising risk management discipline.",
    jay_cred1: "Former Senior Economic Researcher at the International Monetary Fund (IMF)",
    jay_cred2: "Former Head of Systematic Quant Pods — Millennium Management",
    jay_cred3: "System Architect of GARUDA QUANTUM 4D (v1.0 through v6.0)",

    ayana_name: "Aryana Widjaja",
    ayana_role: "Head of Asia-Pacific Macro Research & Digital Risk",
    ayana_bio: "Jakarta Intercultural School (JIS) alumna, BBA Finance from the National University of Singapore (NUS) and MSc Finance from the London School of Economics (LSE) with a thesis on 'AI Applications in Digital Asset Risk Management', supplemented by FinTech research at Cambridge Judge Business School. Bridges cutting-edge quantitative models with Southeast Asian market dynamics.",
    ayana_cred1: "LSE MSc Finance & Cambridge Judge Business School FinTech Research",
    ayana_cred2: "Specialist in Digital Asset Risk Management & AI Quant Modeling",
    ayana_cred3: "Head of Cross-Asset Risk Monitoring for Emerging Markets",

    // Section 5: Pledge
    s5_badge: "Jayendra Halim's Open Letter",
    s5_title: "Why I Returned to Indonesia, and Why This Commitment is Free",
    s5_p1: "I was born in Bandung. Three generations of my family trace their roots to this soil. After three decades navigating the financial capitals of London, Washington DC, and New York, every dialogue with investors in Jakarta brought me face-to-face with a sobering reality: most Indonesian investors still trade on rumors and intuition without disciplined risk shields.",
    s5_p2: "The divide between Wall Street institutions and Indonesian retail investors is not one of intellect or capital, but in <strong>access to systematic quantitative tools and methodologies</strong>.",
    s5_box_title: "GARUDA QUANTUM v3.0 to v6.0 Transition Commitment",
    s5_box_desc: "GARUDA QUANTUM 4D is currently at Version 3.0. During its journey toward Version 6.0, the system requires continuous validation against real Southeast Asian market behavior. Once version 6.0 is complete, I am personally committed to providing access completely free to every member who faithfully studies and practices alongside us.",
    s5_p3: "This is not charity; it is an authentic partnership: you gain an institutional-grade quantitative weapon, the model receives real-world calibration, and together we build the foundation for a future Indonesian Private Equity fund.",
    s5_cta: "Join the Learning Community",
    sig_title: "Global Macro Scholar | Capital Steward",

    // Footer
    foot_brand_desc: "Proprietary multi-dimensional quantitative allocation system for Indonesian investors. Developed by PT Garuda Kuantum Analitika.",
    foot_disclaimer: "Risk Notice: Past performance does not guarantee future results. GARUDA QUANTUM 4D is engineered for quantitative risk analysis and capital management education. Ensure you understand your risk profile and manage liquidity prudently.",
    foot_copy: "© 2026 GARUDA QUANTUM 4D. All Rights Reserved.",
    foot_slogan: "Soar High, Safeguard Your Capital",

    // Community Modal
    modal_title: "Join GARUDA QUANTUM Research Community",
    modal_desc: "Gain direct access to daily model calibrations, macro correlation defense alerts, and interactive research forums with the quantitative desk.",
    modal_email_label: "Private Equity Waitlist & Research v6.0 Access",
    modal_btn_submit: "Register",
    modal_success: "✓ Thank you. The research desk will send your private invitation shortly."
  }
};

let currentLang = 'id';

// ==========================================
// 2. LANGUAGE SWITCHER FUNCTION
// ==========================================
function setLanguage(lang) {
  if (!translations[lang]) return;
  currentLang = lang;
  localStorage.setItem('garuda_lang', lang);

  // Update HTML Lang, Document Title & Meta Description
  document.documentElement.lang = lang;
  if (translations[lang].site_title) {
    document.title = translations[lang].site_title;
  }
  if (translations[lang].site_desc) {
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) metaDesc.setAttribute('content', translations[lang].site_desc);
  }

  // Translate all [data-i18n] nodes
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    const val = translations[lang][key];
    if (val !== undefined) {
      // If string contains HTML (such as <strong> tags), use innerHTML to avoid raw asterisks!
      if (typeof val === 'string' && val.includes('<')) {
        el.innerHTML = val;
      } else {
        el.textContent = val;
      }
    }
  });

  // Update button active state & aria-pressed
  document.querySelectorAll('.lang-btn').forEach(btn => {
    const isActive = btn.getAttribute('data-lang') === lang;
    btn.classList.toggle('active', isActive);
    btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
  });

  // Update simulator explanation according to currently active scenario
  const activeScenBtn = document.querySelector('.scenario-btn.active');
  if (activeScenBtn) {
    const scen = activeScenBtn.getAttribute('data-scenario');
    applyScenario(scen);
  }
}

// ==========================================
// 3. 4D DYNAMIC SIMULATOR LOGIC
// ==========================================
const scenarios = {
  normal: {
    weights: { eq: 35, fi: 30, com: 20, alt: 15 },
    desc: {
      id: "Kondisi pasar seimbang: Bobot terdistribusi proporsional untuk menangkap pertumbuhan tren IHSG/Global (35%), diimbangi cadangan obligasi stabil (30%) dan proteksi komoditas (20%).",
      en: "Balanced Market: Proportional weighting capturing secular IDX/global equity growth (35%), hedged with stable SBN buffers (30%) and commodity resilience (20%)."
    }
  },
  inflation: {
    weights: { eq: 15, fi: 15, com: 55, alt: 15 },
    desc: {
      id: "Guncangan inflasi & Rupiah melemah: Bobot Komoditas (Emas, Nikel, CPO) dinaikkan secara masif hingga 55% sebagai penyerap likuiditas riil, sementara durasi obligasi dipangkas drastis.",
      en: "Inflation & FX Shock: Commodities (Gold, Nickel, CPO) scaled up aggressively to 55% as a real liquidity sponge, while bond duration is trimmed to limit rate sensitivity."
    }
  },
  crash: {
    weights: { eq: 5, fi: 65, com: 25, alt: 5 },
    desc: {
      id: "Krisis Saham Global: Eksposur ekuitas dipangkas ke batas minimal (5%) dan membuka short hedging terukur. Modal diparkir di instrumen likuiditas SBN/US Treasuries (65%) untuk keselamatan mutlak.",
      en: "Global Equity Crash: Equity beta trimmed to a strict 5% with short hedging. Capital is shielded inside sovereign SBN/US Treasuries (65%) to secure dry powder."
    }
  },
  crypto: {
    weights: { eq: 30, fi: 25, com: 20, alt: 25 },
    desc: {
      id: "Reli Siklus Kripto: Eksposur aset digital dinaikkan ke batas atas batas risiko (25%) dengan trailing stop terkuantisasi, memanfaatkan momentum asimetris tanpa mengorbankan bantalan obligasi.",
      en: "Crypto Cycle Expansion: Digital asset allocation scaled up to its risk ceiling (25%) with algorithmic trailing stops, capturing convexity while preserving fixed income buffers."
    }
  }
};

function applyScenario(scenKey) {
  const scen = scenarios[scenKey];
  if (!scen) return;

  // Update button active state & aria-selected
  document.querySelectorAll('.scenario-btn').forEach(btn => {
    const isSelected = btn.getAttribute('data-scenario') === scenKey;
    btn.classList.toggle('active', isSelected);
    btn.setAttribute('aria-selected', isSelected ? 'true' : 'false');
  });

  // Animate weights
  const { eq, fi, com, alt } = scen.weights;
  
  const valEq = document.getElementById('val-eq');
  const valFi = document.getElementById('val-fi');
  const valCom = document.getElementById('val-com');
  const valAlt = document.getElementById('val-alt');

  const fillEq = document.getElementById('fill-eq');
  const fillFi = document.getElementById('fill-fi');
  const fillCom = document.getElementById('fill-com');
  const fillAlt = document.getElementById('fill-alt');

  if (valEq) valEq.textContent = `${eq}%`;
  if (valFi) valFi.textContent = `${fi}%`;
  if (valCom) valCom.textContent = `${com}%`;
  if (valAlt) valAlt.textContent = `${alt}%`;

  if (fillEq) fillEq.style.width = `${eq}%`;
  if (fillFi) fillFi.style.width = `${fi}%`;
  if (fillCom) fillCom.style.width = `${com}%`;
  if (fillAlt) fillAlt.style.width = `${alt}%`;

  const expEl = document.getElementById('sim-explanation-text');
  if (expEl) {
    expEl.textContent = scen.desc[currentLang] || scen.desc.id;
  }
}

// ==========================================
// 4. ARCHITECTURAL ENTRANCE TIMELINE (Compressed & Snappy)
// ==========================================
let entranceTimeline = null;

function skipEntranceAnimation() {
  if (entranceTimeline) {
    entranceTimeline.kill();
  }
  const surface = document.querySelector('.page-reveal-surface');
  const legacyView = document.querySelector('.legacy-view');
  const scrim = document.querySelector('.page-reveal-scrim');

  if (surface) {
    surface.classList.add('hero-revealed');
    if (window.gsap) {
      gsap.set(surface, { clearProps: "transform,scale,clipPath,willChange,visibility" });
    } else {
      surface.style.visibility = 'visible';
      surface.style.transform = 'none';
      surface.style.overflowY = 'auto';
      surface.style.pointerEvents = 'auto';
    }
  }
  if (legacyView) legacyView.style.display = 'none';
  if (scrim) scrim.style.display = 'none';

  sessionStorage.setItem('garuda_intro_viewed', 'true');
}

function runEntranceAnimation(force = false) {
  // Respect reduced motion
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    skipEntranceAnimation();
    return;
  }

  // If already viewed in current session and not forced by replay button, skip immediately
  if (!force && sessionStorage.getItem('garuda_intro_viewed') === 'true') {
    skipEntranceAnimation();
    return;
  }

  // If GSAP failed to load, unlock safely
  if (!window.gsap) {
    document.documentElement.classList.add('no-gsap');
    skipEntranceAnimation();
    return;
  }

  const legacyView = document.querySelector('.legacy-view');
  const scrim = document.querySelector('.page-reveal-scrim');
  const surface = document.querySelector('.page-reveal-surface');
  const wordmark = document.querySelector('.brand-wordmark');
  const wordmarkWrap = document.querySelector('.brand-wordmark-container');
  const emblem = document.querySelector('.brand-emblem');
  const quadTiles = document.querySelectorAll('.quad-tile');
  const navbar = document.querySelector('.site-navbar');
  const heroLeft = document.querySelector('.hero-left-col');
  const heroRight = document.querySelector('.hero-right-col');

  if (!surface || !legacyView) return;

  // Kill existing timeline if active
  if (entranceTimeline) {
    entranceTimeline.kill();
  }

  // Scroll back to top on replay
  surface.scrollTop = 0;
  window.scrollTo(0, 0);

  // Initial resets
  legacyView.style.display = 'flex';
  if (scrim) scrim.style.display = 'block';
  surface.classList.remove('hero-revealed');

  gsap.set(legacyView, { yPercent: 0, opacity: 1 });
  gsap.set(scrim, { opacity: 0 });
  gsap.set(surface, {
    yPercent: 100,
    scale: 0.97,
    clipPath: 'inset(8% round 20px)',
    visibility: 'visible',
    overflowY: 'hidden',
    pointerEvents: 'none'
  });

  gsap.set('.line-horizontal', { scaleX: 0 });
  gsap.set('.line-vertical', { scaleY: 0 });
  gsap.set('.shared-gradient-composition', { scale: 0.05, opacity: 0 });
  gsap.set(quadTiles, { opacity: 0, scale: 0.6 });
  gsap.set(wordmarkWrap, { opacity: 0 });
  gsap.set(emblem, { rotation: 0, scale: 1 });

  if (wordmark) wordmark.textContent = "GARUDA";

  // Build Snappy Master Timeline (~2.2s total)
  entranceTimeline = gsap.timeline({
    defaults: { ease: "power3.out" },
    onComplete: () => {
      surface.classList.add('hero-revealed');
      legacyView.style.display = 'none';
      if (scrim) scrim.style.display = 'none';
      gsap.set(surface, { clearProps: "transform,scale,clipPath,willChange" });
      sessionStorage.setItem('garuda_intro_viewed', 'true');
    }
  });

  // Phase 1: Core expansion & construction lines
  entranceTimeline
    .to('.shared-gradient-composition', {
      scale: 1,
      opacity: 1,
      duration: 0.45,
      ease: "back.out(1.4)"
    }, 0.05)
    .to('.line-top, .line-bottom, .guide-inner-top, .guide-inner-bottom', {
      scaleX: 1,
      duration: 0.4,
      stagger: 0.05
    }, 0.15)
    .to('.line-left, .line-right, .guide-inner-left, .guide-inner-right', {
      scaleY: 1,
      duration: 0.4,
      stagger: 0.05
    }, 0.18)

    // Phase 2: Splitting into 4 dimensions
    .to(quadTiles, {
      opacity: 1,
      scale: 1,
      stagger: 0.04,
      duration: 0.35,
      ease: "power2.out"
    }, 0.35)

    // Phase 3: Rotate Emblem 360° (settles upright) + Typing Wordmark
    .to(emblem, {
      rotation: 360,
      scale: 1,
      duration: 0.65,
      ease: "power2.inOut"
    }, 0.65)
    .to(wordmarkWrap, {
      opacity: 1,
      duration: 0.25
    }, 0.72)
    .call(() => { if (wordmark) wordmark.textContent = "GARUDA"; }, null, 0.72)
    .call(() => { if (wordmark) wordmark.textContent = "GARUDA QUANTUM"; }, null, 0.92)
    .call(() => { if (wordmark) wordmark.textContent = "GARUDA QUANTUM 4D"; }, null, 1.15)

    // Fade construction lines
    .to('.construction-line', {
      opacity: 0,
      duration: 0.3
    }, 1.25)

    // Phase 4: Page reveal surface rises up
    .to(legacyView, {
      yPercent: -22,
      duration: 0.85,
      ease: "power3.inOut"
    }, 1.35)
    .to(scrim, {
      opacity: 1,
      duration: 0.4
    }, 1.35)
    .to(surface, {
      yPercent: 0,
      scale: 1.0,
      clipPath: 'inset(0% round 0px)',
      duration: 0.85,
      ease: "power4.out"
    }, 1.35)

    // Cascade Navbar & Hero Columns
    .fromTo(navbar,
      { y: -24, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.5, ease: "power2.out" },
      1.75
    )
    .fromTo([heroLeft, heroRight],
      { y: 20, opacity: 0 },
      { y: 0, opacity: 1, stagger: 0.08, duration: 0.55, ease: "power3.out" },
      1.85
    );
}

// ==========================================
// 5. COMMUNITY MODAL & DIALOG CONTROLLERS
// ==========================================
function openCommunityModal() {
  const modal = document.getElementById('community-modal');
  if (modal) {
    modal.classList.add('is-open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }
}

function closeCommunityModal() {
  const modal = document.getElementById('community-modal');
  if (modal) {
    modal.classList.remove('is-open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }
}

// ==========================================
// 6. SCROLL REVEAL (IntersectionObserver)
// ==========================================
function initScrollReveal() {
  if (!('IntersectionObserver' in window)) {
    document.querySelectorAll('.reveal-on-scroll').forEach(el => el.classList.add('is-revealed'));
    return;
  }

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-revealed');
        obs.unobserve(entry.target);
      }
    });
  }, {
    rootMargin: '0px 0px -40px 0px',
    threshold: 0.12
  });

  document.querySelectorAll('.reveal-on-scroll').forEach(el => observer.observe(el));
}

// ==========================================
// 7. INITIALIZATION & EVENT LISTENERS
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
  // 1. Skip Intro Button
  const skipBtn = document.getElementById('btn-skip-intro');
  if (skipBtn) {
    skipBtn.addEventListener('click', skipEntranceAnimation);
  }

  // 2. Language Switcher Buttons
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const lang = btn.getAttribute('data-lang');
      setLanguage(lang);
    });
  });

  // 3. Scenario Selector Buttons
  document.querySelectorAll('.scenario-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const scen = btn.getAttribute('data-scenario');
      applyScenario(scen);
    });
  });

  // 4. Mobile Menu Toggle
  const mobileToggle = document.getElementById('mobile-toggle');
  const mobileDrawer = document.getElementById('mobile-drawer');
  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      const isOpen = mobileDrawer.classList.toggle('is-open');
      mobileToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
    // Close drawer when clicking any link inside it
    mobileDrawer.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileDrawer.classList.remove('is-open');
        mobileToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // 5. Community Modal Wiring
  const openButtons = [
    'btn-open-community-nav',
    'btn-open-community-mobile',
    'btn-hero-community',
    'btn-pledge-community',
    'btn-footer-waitlist'
  ];
  openButtons.forEach(id => {
    const btn = document.getElementById(id);
    if (btn) btn.addEventListener('click', openCommunityModal);
  });

  const closeBtn = document.getElementById('modal-close-btn');
  const modalBackdrop = document.getElementById('community-modal');
  if (closeBtn) closeBtn.addEventListener('click', closeCommunityModal);
  if (modalBackdrop) {
    modalBackdrop.addEventListener('click', (e) => {
      if (e.target === modalBackdrop) closeCommunityModal();
    });
  }

  // ESC key to close modal
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeCommunityModal();
  });

  // Waitlist Form Handler
  const wlForm = document.getElementById('waitlist-form');
  if (wlForm) {
    wlForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const successMsg = document.getElementById('form-success-msg');
      if (successMsg) successMsg.style.display = 'block';
      const input = document.getElementById('wl-email');
      if (input) input.value = '';
    });
  }

  // 6. Replay Entrance Animation Button
  const replayBtn = document.getElementById('btn-replay-intro');
  if (replayBtn) {
    replayBtn.addEventListener('click', () => {
      runEntranceAnimation(true);
    });
  }

  // 7. Initial Language Setup from localStorage or default 'id'
  const savedLang = localStorage.getItem('garuda_lang') || 'id';
  setLanguage(savedLang);
  applyScenario('normal');

  // 8. Initialize Scroll Reveal Observer
  initScrollReveal();

  // 9. Smooth Scroll for in-page anchors
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#' || targetId === '') return;
      const targetEl = document.querySelector(targetId);
      const surface = document.querySelector('.page-reveal-surface');
      if (targetEl && surface) {
        e.preventDefault();
        const navHeight = document.querySelector('.site-navbar')?.offsetHeight || 72;
        const targetTop = targetEl.offsetTop - navHeight;
        surface.scrollTo({
          top: Math.max(0, targetTop),
          behavior: 'smooth'
        });
      }
    });
  });

  // 10. Trigger Entrance Animation
  runEntranceAnimation();
});
"""

with open(r'c:\Users\Administrator\Desktop\新建文件夹 (5)\app.js', 'w', encoding='utf-8') as f:
    f.write(app_content)

print("Updated app.js successfully!")
