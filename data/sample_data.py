"""Synthetic sample financial articles with ground-truth company tags.

These articles are fictional but realistic, covering the target companies
for the news tagging demo.
"""

from datetime import datetime, timezone

from app.database.models import Article, Company, ArticleCompany


# ---------------------------------------------------------------------------
# Companies (ground truth)
# ---------------------------------------------------------------------------

COMPANIES: list[dict] = [
    {
        "canonical_name": "NVIDIA",
        "ticker": "NVDA",
        "aliases": '["Nvidia", "NVDA Corp", "NVIDIA Corp"]',
    },
    {
        "canonical_name": "Advanced Micro Devices",
        "ticker": "AMD",
        "aliases": '["AMD", "AMD Inc", "Advanced Micro Devices Inc"]',
    },
    {
        "canonical_name": "Microsoft",
        "ticker": "MSFT",
        "aliases": '["MSFT", "Microsoft Corp", "Microsoft Corporation"]',
    },
    {
        "canonical_name": "Apple",
        "ticker": "AAPL",
        "aliases": '["AAPL", "Apple Inc", "Apple Corporation"]',
    },
    {
        "canonical_name": "Taiwan Semiconductor Manufacturing",
        "ticker": "TSM",
        "aliases": '["TSMC", "Taiwan Semi", "TSM"]',
    },
    {
        "canonical_name": "Intel",
        "ticker": "INTC",
        "aliases": '["INTC", "Intel Corp", "Intel Corporation"]',
    },
    {
        "canonical_name": "Qualcomm",
        "ticker": "QCOM",
        "aliases": '["QCOM", "Qualcomm Inc", "Qualcomm Corporation"]',
    },
    {
        "canonical_name": "Alphabet",
        "ticker": "GOOG",
        "aliases": '["Google", "Google LLC", "Alphabet Inc"]',
    },
    {
        "canonical_name": "Amazon",
        "ticker": "AMZN",
        "aliases": '["AMZN", "Amazon.com", "Amazon Web Services", "AWS"]',
    },
    {
        "canonical_name": "Meta Platforms",
        "ticker": "META",
        "aliases": '["META", "Facebook", "Meta", "Meta Platforms Inc"]',
    },
]


# ---------------------------------------------------------------------------
# Articles with ground-truth company links
# Format: (article_dict, [company_id_1, company_id_2, ...])
# ---------------------------------------------------------------------------

ARTICLES: list[tuple[dict, list[int]]] = [
    (
        {
            "title": "NVIDIA Unveils Next-Generation AI GPU at GTC 2026",
            "source": "TechCrunch",
            "url": "https://example.com/nvidia-gtc-2026",
            "published_at": datetime(2026, 3, 18, 9, 0, tzinfo=timezone.utc),
            "content": (
                "NVIDIA today unveiled its next-generation AI accelerator GPU, "
                "the Blackwell Ultra, promising a 3x performance improvement over "
                "the previous generation. The chip is designed for large language "
                "model training and inference. NVIDIA CEO Jensen Huang stated that "
                "demand from cloud providers and enterprise customers continues to "
                "outpace supply. Microsoft and Google have already committed to "
                "deploying the new chips in their data centers."
            ),
        },
        [1, 3, 8],
    ),
    (
        {
            "title": "AMD Gains Market Share in Data Center CPUs",
            "source": "Reuters",
            "url": "https://example.com/amd-datacenter-share",
            "published_at": datetime(2026, 3, 20, 14, 30, tzinfo=timezone.utc),
            "content": (
                "Advanced Micro Devices reported its strongest quarter for EPYC "
                "server processors, gaining 18% market share in the data center "
                "CPU segment. AMD's gains come at the expense of Intel, which "
                "has struggled to compete with its Zen-based architectures. "
                "Analysts note that AMD's partnership with Microsoft on custom "
                "chips for Azure has also bolstered its enterprise credibility."
            ),
        },
        [2, 3, 6],
    ),
    (
        {
            "title": "Apple Unveils AI-Powered MacBook with Custom Silicon",
            "source": "The Verge",
            "url": "https://example.com/apple-macbook-ai",
            "published_at": datetime(2026, 3, 22, 10, 0, tzinfo=timezone.utc),
            "content": (
                "Apple introduced a new line of MacBooks powered by its next-gen "
                "M-series chip, featuring a dedicated neural engine for on-device "
                "AI workloads. The company emphasized privacy, stating that all AI "
                "processing happens locally. Apple's stock rose 4% on the news. "
                "The new MacBooks will compete directly with Microsoft Surface "
                "and Intel-powered ultrabooks."
            ),
        },
        [4, 3, 6],
    ),
    (
        {
            "title": "TSMC Announces $40 Billion Expansion in Arizona",
            "source": "Bloomberg",
            "url": "https://example.com/tsmc-arizona-expansion",
            "published_at": datetime(2026, 3, 25, 8, 0, tzinfo=timezone.utc),
            "content": (
                "Taiwan Semiconductor Manufacturing Company announced a massive "
                "expansion of its Arizona fabrication facilities, investing $40 "
                "billion to build three new 3nm fabs. The move is part of a "
                "global effort to diversify semiconductor supply chains away "
                "from geopolitical risk. NVIDIA and AMD are expected to be "
                "among the primary customers for the new capacity."
            ),
        },
        [5, 1, 2],
    ),
    (
        {
            "title": "Intel Secures $15 Billion CHIPS Act Funding Boost",
            "source": "Wall Street Journal",
            "url": "https://example.com/intel-chips-act",
            "published_at": datetime(2026, 4, 1, 11, 0, tzinfo=timezone.utc),
            "content": (
                "The U.S. Commerce Department approved an additional $15 billion "
                "in CHIPS Act funding for Intel, supporting its Ohio fab "
                "expansion. Intel CEO Pat Gelsinger said the funding will help "
                "the company catch up to TSMC in manufacturing technology. "
                "The announcement was welcomed by AMD, which benefits from a "
                "competitive, diversified foundry landscape."
            ),
        },
        [6, 5, 2],
    ),
    (
        {
            "title": "Qualcomm Partners with Microsoft on AI PCs",
            "source": "CNBC",
            "url": "https://example.com/qualcomm-microsoft-ai-pc",
            "published_at": datetime(2026, 4, 5, 9, 30, tzinfo=timezone.utc),
            "content": (
                "Qualcomm and Microsoft announced a deepened partnership to "
                "develop Snapdragon-based AI PCs that can run large language "
                "models locally. The chips are expected to offer significantly "
                "better battery life than Intel and AMD competitors. Apple has "
                "also been exploring ARM-based PC chips, though its custom silicon "
                "strategy keeps it separate from this partnership."
            ),
        },
        [7, 3, 6, 4],
    ),
    (
        {
            "title": "Google DeepMind Releases Open-Source AI Model",
            "source": "TechCrunch",
            "url": "https://example.com/google-deepmind-open-source",
            "published_at": datetime(2026, 4, 10, 7, 0, tzinfo=timezone.utc),
            "content": (
                "Google's DeepMind division released a powerful open-source "
                "foundation model for natural language and code generation. "
                "The model competes with offerings from Microsoft's OpenAI "
                "partnership and Meta's Llama series. NVIDIA GPUs are expected "
                "to be the primary training hardware. Amazon's AWS and Microsoft "
                "Azure both announced immediate support for deploying the model."
            ),
        },
        [8, 3, 1, 9, 10],
    ),
    (
        {
            "title": "Amazon Web Services Launches New AI Infrastructure",
            "source": "Reuters",
            "url": "https://example.com/aws-ai-infra",
            "published_at": datetime(2026, 4, 15, 12, 0, tzinfo=timezone.utc),
            "content": (
                "Amazon Web Services unveiled a new generation of AI training "
                "instances powered by custom silicon and NVIDIA GPUs. The new "
                "infrastructure is designed to reduce the cost of training large "
                "language models by 40%. Competitors Microsoft Azure and Google "
                "Cloud have been engaged in a similar arms race, investing "
                "billions in AI infrastructure."
            ),
        },
        [9, 1, 3, 8],
    ),
    (
        {
            "title": "Meta Invests $30 Billion in AI Research for 2026",
            "source": "Bloomberg",
            "url": "https://example.com/meta-ai-investment",
            "published_at": datetime(2026, 4, 20, 10, 0, tzinfo=timezone.utc),
            "content": (
                "Meta Platforms announced a $30 billion AI research budget for "
                "2026, up from $20 billion in 2025. CEO Mark Zuckerberg said "
                "the company is betting heavily on open-source AI models and "
                "metaverse applications. Meta's AI models are trained on "
                "custom chips and NVIDIA GPUs, with infrastructure spanning "
                "Amazon AWS and Google Cloud data centers."
            ),
        },
        [10, 1, 9, 8],
    ),
    (
        {
            "title": "AMD and NVIDIA Compete in AI Chip Market",
            "source": "Financial Times",
            "url": "https://example.com/amd-nvidia-competition",
            "published_at": datetime(2026, 4, 25, 8, 30, tzinfo=timezone.utc),
            "content": (
                "AMD's latest MI350 AI accelerator is gaining traction among "
                "cloud providers as a cost-effective alternative to NVIDIA's "
                "dominant H100 chip. Market analysts predict AMD could capture "
                "15% of the AI accelerator market by end of 2026. Microsoft "
                "has been an early adopter of AMD's custom chips for Azure. "
                "Intel's AI chip efforts, including the Gaudi series, have "
                "gained limited adoption."
            ),
        },
        [1, 2, 3, 6],
    ),
    (
        {
            "title": "Apple Reports Record Revenue Amid AI Push",
            "source": "Wall Street Journal",
            "url": "https://example.com/apple-revenue-record",
            "published_at": datetime(2026, 5, 1, 7, 0, tzinfo=timezone.utc),
            "content": (
                "Apple reported record quarterly revenue of $128 billion, "
                "driven by strong iPhone 17 sales and growing services revenue. "
                "The company's AI strategy, centered on on-device processing "
                "with its custom silicon, has been well-received by privacy-"
                "concerned consumers. Apple continues to rely on NVIDIA for "
                "some cloud-based AI workloads."
            ),
        },
        [4, 1],
    ),
    (
        {
            "title": "TSMC and Samsung Race for 2nm Chip Production",
            "source": "Nikkei Asia",
            "url": "https://example.com/tsmc-samsung-2nm",
            "published_at": datetime(2026, 5, 5, 9, 0, tzinfo=timezone.utc),
            "content": (
                "TSMC is on track to begin 2nm chip production in late 2026, "
                "with Apple and NVIDIA as the first customers. Samsung's rival "
                "2nm process is expected to lag by several months. The race for "
                "smaller transistors is critical for the next generation of AI "
                "chips. AMD and Intel have also signed supply agreements with "
                "TSMC for future process nodes."
            ),
        },
        [5, 4, 1, 2, 6],
    ),
    (
        {
            "title": "Intel Launches New AI Chip to Challenge NVIDIA",
            "source": "The Register",
            "url": "https://example.com/intel-ai-chip-launch",
            "published_at": datetime(2026, 5, 10, 11, 0, tzinfo=timezone.utc),
            "content": (
                "Intel unveiled its latest AI accelerator, the Gaudi 4, claiming "
                "competitive performance at a lower price point than NVIDIA's "
                "H200. While Intel has struggled in the data center GPU market, "
                "the company is banking on CHIPS Act funding and U.S. government "
                "contracts to gain traction. Microsoft and Amazon have expressed "
                "interest in testing the new chip."
            ),
        },
        [6, 1, 3, 9],
    ),
    (
        {
            "title": "Qualcomm Expands AI PC Chip Portfolio",
            "source": "ZDNet",
            "url": "https://example.com/qualcomm-ai-pc-portfolio",
            "published_at": datetime(2026, 5, 15, 10, 30, tzinfo=timezone.utc),
            "content": (
                "Qualcomm expanded its AI PC processor lineup with the Snapdragon "
                "X Elite Gen 2, targeting both consumer and enterprise markets. "
                "The chip promises up to 20 hours of battery life on laptops. "
                "Qualcomm's push into AI PCs positions it as a direct competitor "
                "to Intel and AMD in the laptop CPU market, while also partnering "
                "with Microsoft on optimized AI workloads."
            ),
        },
        [7, 6, 2, 3],
    ),
    (
        {
            "title": "Google Cloud Wins Major AI Contract with Microsoft",
            "source": "TechCrunch",
            "url": "https://example.com/google-microsoft-ai-contract",
            "published_at": datetime(2026, 5, 20, 8, 0, tzinfo=timezone.utc),
            "content": (
                "In a surprising partnership, Microsoft signed a multi-year "
                "agreement to use Google Cloud's AI infrastructure for select "
                "workloads. The deal includes access to Google's TPU v5 chips "
                "and DeepMind models. The partnership also involves NVIDIA GPUs "
                "for specific training tasks. Amazon Web Services and Meta have "
                "both been active in competing for similar enterprise AI contracts."
            ),
        },
        [8, 3, 1, 9, 10],
    ),
    (
        {
            "title": "NVIDIA Revenue Surges on AI Demand",
            "source": "CNBC",
            "url": "https://example.com/nvidia-revenue-surge",
            "published_at": datetime(2026, 6, 1, 7, 30, tzinfo=timezone.utc),
            "content": (
                "NVIDIA reported quarterly revenue of $38 billion, a 120% "
                "year-over-year increase, driven by insatiable demand for AI "
                "chips. The company's data center segment alone generated $32 "
                "billion. Major customers include Microsoft, Amazon, Google, "
                "and Meta. NVIDIA's dominance in AI accelerators remains "
                "uncontested, though AMD and Intel continue to develop "
                "competitive alternatives."
            ),
        },
        [1, 3, 9, 8, 10],
    ),
    (
        {
            "title": "AMD Announces New Ryzen AI Processors for Consumers",
            "source": "Tom's Hardware",
            "url": "https://example.com/amd-ryzen-ai",
            "published_at": datetime(2026, 6, 10, 9, 0, tzinfo=timezone.utc),
            "content": (
                "AMD launched its Ryzen AI 300 series processors for consumer "
                "laptops, featuring an integrated NPU for on-device AI tasks. "
                "The chips target the same market as Qualcomm's Snapdragon X and "
                "Intel's Core Ultra processors. AMD also highlighted its "
                "partnership with Microsoft to optimize Windows for AMD AI "
                "workloads. Apple continues to use its own M-series chips in "
                "MacBooks, keeping it separate from the Windows ecosystem."
            ),
        },
        [2, 7, 6, 3, 4],
    ),
    (
        {
            "title": "Apple and TSMC Deepen Custom Chip Partnership",
            "source": "Bloomberg",
            "url": "https://example.com/apple-tsmc-custom-chip",
            "published_at": datetime(2026, 6, 15, 10, 0, tzinfo=timezone.utc),
            "content": (
                "Apple and TSMC are collaborating on a new generation of custom "
                "AI accelerators for future iPhones and iPads. The chips will "
                "be manufactured using TSMC's 2nm process. Apple's strategy of "
                "designing its own silicon has allowed it to reduce reliance on "
                "Intel and Qualcomm for certain workloads, though NVIDIA remains "
                "a key supplier for cloud AI infrastructure."
            ),
        },
        [4, 5, 6, 7, 1],
    ),
    (
        {
            "title": "Meta's Llama 4 Opens New Frontiers in Open-Source AI",
            "source": "VentureBeat",
            "url": "https://example.com/meta-llama-4",
            "published_at": datetime(2026, 6, 20, 8, 30, tzinfo=timezone.utc),
            "content": (
                "Meta released Llama 4, a 400-billion-parameter open-source "
                "language model that rivals proprietary models from Google and "
                "Microsoft. The model was trained on NVIDIA GPUs across Meta's "
                "own data centers and Amazon AWS infrastructure. Amazon and "
                "Google Cloud both announced support for deploying Llama 4. "
                "The open-source approach has been praised by the AI community "
                "and positions Meta as a leader in democratizing AI."
            ),
        },
        [10, 1, 9, 8],
    ),
    (
        {
            "title": "AMD and TSMC Announce Joint AI Chip Development",
            "source": "Reuters",
            "url": "https://example.com/amd-tsmc-joint-ai-chip",
            "published_at": datetime(2026, 6, 25, 11, 0, tzinfo=timezone.utc),
            "content": (
                "AMD and TSMC announced a joint development program for custom "
                "AI accelerators tailored for cloud providers. The first chips "
                "are expected in 2027 and will target Microsoft Azure and "
                "Amazon AWS. The partnership strengthens AMD's position against "
                "Intel in the data center market and provides an alternative to "
                "NVIDIA's dominant AI chip ecosystem."
            ),
        },
        [2, 5, 3, 9, 6, 1],
    ),
    (
        {
            "title": "Google Unveils Next-Gen TPU for AI Training",
            "source": "The Verge",
            "url": "https://example.com/google-tpu-next-gen",
            "published_at": datetime(2026, 7, 1, 9, 0, tzinfo=timezone.utc),
            "content": (
                "Google announced its next-generation TPU v6, designed for "
                "large-scale AI training. The chip delivers 4x the performance "
                "of TPU v5 and is optimized for transformer models. Google plans "
                "to make TPU v6 available through Google Cloud and has already "
                "secured commitments from Microsoft and Amazon for shared "
                "deployment. NVIDIA's GPUs remain the industry standard, but "
                "Google's custom silicon is gaining ground."
            ),
        },
        [8, 3, 9, 1],
    ),
    (
        {
            "title": "Intel CEO Outlines Ambitious Foundry Expansion Plan",
            "source": "Financial Times",
            "url": "https://example.com/intel-foundry-expansion",
            "published_at": datetime(2026, 7, 10, 7, 30, tzinfo=timezone.utc),
            "content": (
                "Intel CEO Pat Gelsinger presented a plan to expand Intel's "
                "foundry business to serve external customers, including AMD, "
                "Qualcomm, and even NVIDIA. The company is investing $100 "
                "billion over five years to build four new fabs in the U.S. "
                "The move is critical for Intel's turnaround and aims to close "
                "the technology gap with TSMC. Microsoft has already signed a "
                "supply agreement for custom chips."
            ),
        },
        [6, 2, 7, 1, 5, 3],
    ),
    (
        {
            "title": "Apple Launches AI-Powered Siri with On-Device Processing",
            "source": "Wired",
            "url": "https://example.com/apple-ai-siri",
            "published_at": datetime(2026, 7, 15, 10, 0, tzinfo=timezone.utc),
            "content": (
                "Apple unveiled a completely redesigned Siri powered by on-device "
                "AI using Apple's custom neural engine. The new Siri can handle "
                "complex tasks without sending data to the cloud, distinguishing "
                "it from Google Assistant and Amazon Alexa. Apple's M-series and "
                "A-series chips are central to this strategy. The company also "
                "announced partnerships with NVIDIA for cloud-based AI tasks "
                "that exceed on-device capabilities."
            ),
        },
        [4, 1],
    ),
    (
        {
            "title": "Qualcomm and TSMC Partner on Next-Gen Mobile AI Chips",
            "source": "Nikkei Asia",
            "url": "https://example.com/qualcomm-tsmc-mobile-ai",
            "published_at": datetime(2026, 7, 20, 8, 0, tzinfo=timezone.utc),
            "content": (
                "Qualcomm and TSMC announced a partnership to develop next-"
                "generation mobile AI chips for smartphones and wearables. "
                "The chips will be manufactured on TSMC's 2nm process and "
                "feature a dedicated AI accelerator. Apple has been a long-"
                "time TSMC customer for its custom silicon. Intel's mobile chip "
                "business has largely been phased out, while AMD focuses on PC "
                "and data center markets."
            ),
        },
        [7, 5, 4, 6, 2],
    ),
    (
        {
            "title": "Amazon and Microsoft Expand Cloud AI Partnership",
            "source": "Bloomberg",
            "url": "https://example.com/aws-azure-ai-partnership",
            "published_at": datetime(2026, 7, 25, 11, 30, tzinfo=timezone.utc),
            "content": (
                "Amazon Web Services and Microsoft Azure announced an expanded "
                "partnership to enable hybrid cloud AI deployments. The "
                "collaboration allows customers to seamlessly run AI workloads "
                "across both platforms. Both companies have been investing "
                "heavily in AI infrastructure, with AWS deploying NVIDIA GPUs "
                "and Azure using a mix of NVIDIA and AMD chips. Google Cloud "
                "and Meta's infrastructure remain key competitors in the space."
            ),
        },
        [9, 3, 1, 2, 8, 10],
    ),
]


def load_sample_data(db) -> dict:
    """Load synthetic sample data into the database.

    Returns a dict with counts: {articles: N, companies: M, links: L}
    """
    from sqlalchemy import inspect

    inspector = inspect(db.get_bind())
    tables = inspector.get_table_names()

    # Skip if data already exists
    if "companies" in tables and "articles" in tables:
        existing_articles = db.query(Article).count()
        if existing_articles > 0:
            return {"articles": existing_articles, "companies": db.query(Company).count(), "links": db.query(ArticleCompany).count()}

    # Create tables if they don't exist
    from app.database.database import Base
    Base.metadata.create_all(db.get_bind())

    # Insert companies
    company_map: dict[str, int] = {}
    for comp_data in COMPANIES:
        existing = db.query(Company).filter_by(canonical_name=comp_data["canonical_name"]).first()
        if existing:
            company_map[comp_data["canonical_name"]] = existing.id
        else:
            company = Company(**comp_data)
            db.add(company)
            db.flush()
            company_map[comp_data["canonical_name"]] = company.id

    # Insert articles and links
    article_map: dict[str, int] = {}
    article_links: list[tuple[dict, list[int]]] = ARTICLES

    for article_data, company_ids in article_links:
        existing = db.query(Article).filter_by(title=article_data["title"]).first()
        if existing:
            article_map[article_data["title"]] = existing.id
            continue
        article = Article(**article_data)
        db.add(article)
        db.flush()
        article_map[article_data["title"]] = article.id

        for company_id in company_ids:
            link = ArticleCompany(
                article_id=article.id,
                company_id=company_id,
                tagging_method="manual",
                confidence=1.0,
                evidence="Ground truth (manual annotation)",
            )
            db.add(link)

    db.commit()
    return {
        "articles": len(article_map),
        "companies": len(company_map),
        "links": db.query(ArticleCompany).count(),
    }
