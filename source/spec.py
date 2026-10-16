"""Luca AI product documentation v1 — the single source of truth for what is documented.

Rule: only parameters MaximusLabs is CERTAIN Luca has are documented.
  available = ✅ on founder / product evidence
  scoped    = 🟡 — certain it exists, in a narrower form than a buyer might assume; the scope
              sentence is mandatory and is shown on the page
Everything else (❓ 🗺 🛠 ❌, and every overclaim on ask-luca.com) is NOT documented. It goes to
the client worksheet (build_worksheet.py) for Luca's team to fill.

Never documented as available, whatever the website says: autonomous execution / autonomy levels,
proactive alerts, memory, forecasting, scenario modelling, capital availability or terms, prices,
SOC 2, EU data residency, connector counts.
"""

DATE = "2026-10-16"

# Evidence sources, cited by key in FACTS.
SRC = {
    "deck": "Luca Labs investor presentation, May 2026 — Connect & Setup product screenshot (slide 5)",
    "c0522": "Weekly call, 2026-05-22 (Eric Bidinger)",
    "c0605": "Weekly call, 2026-06-05",
    "c0717": "Weekly call, 2026-07-17",
    "c0724": "Weekly call, 2026-07-24",
    "c0807": "Weekly call, 2026-08-07",
    "c0904": "Weekly call, 2026-09-04",
    "c0918": "Weekly call, 2026-09-18",
    "c0925": "Weekly call, 2026-09-25",
    "c1002": "Weekly call, 2026-10-02 (Numbers demo and Usman's product walkthrough)",
    "henrik": "Eric Bidinger sales conversation with Henrik Jonsson, 2026-06-04",
    "ecc": "Eric call context transcript, ~June 2026",
    "news": "Luca client newsletter, 2026-10-12",
    "site": "ask-luca.com, read 2026-10-16",
    "rivo": "Rivo / Saras '10 Best AI Analytics Tools for Shopify Brands', 2026-09-26",
    "privacy": "ask-luca.com/privacy, read 2026-10-16",
    "pricing": "ask-luca.com/pricing, read 2026-10-16",
    "about": "ask-luca.com/about, read 2026-10-16",
    "mc": "Mastercard Business Bonus listing shown by Eric, 2026-10-02",
    "community": "Eric's community invitation email, 2026-08-25",
    "positioning": "Eric's canonical positioning statement (Site Structure V2): 'We are not a financing company. We are an Agentic AI company for e-commerce.'",
}

# ---------------------------------------------------------------------------
# Pages. type: hub | product | feature | integration | solution | pricing | security | support | review
# ---------------------------------------------------------------------------
PAGES = [
    # Start
    dict(url="/", title="Luca AI product documentation", nav="Start here", type="home"),
    # Products
    dict(url="/products/", title="Products", nav="Products", type="hub"),
    dict(url="/products/luca-agent/", title="Luca, the AI analyst agent", nav="Luca agent", type="product"),
    dict(url="/products/numbers/", title="Numbers: the reconciled control centre", nav="Numbers", type="product"),
    dict(url="/products/knowledge-base/", title="Knowledge base and business context", nav="Knowledge base", type="product"),
    dict(url="/products/capital/", title="Capital, and how it relates to Luca", nav="Capital", type="product"),
    dict(url="/products/features/", title="Feature directory", nav="Feature directory", type="hub"),
    dict(url="/products/features/data-connection/", title="Data connection and setup", nav="Data connection", type="feature"),
    dict(url="/products/features/control-and-safety/", title="Control and safety: Luca reads, you decide", nav="Control and safety", type="feature"),
    dict(url="/products/features/teams-and-seats/", title="Teams, seats and regions", nav="Teams and seats", type="feature"),
    # Integrations
    dict(url="/integrations/", title="Integrations", nav="Integrations", type="hub"),
    dict(url="/integrations/commerce/", title="Commerce platforms", nav="Commerce", type="hub"),
    dict(url="/integrations/commerce/shopify/", title="Shopify", nav="Shopify", type="integration"),
    dict(url="/integrations/commerce/amazon/", title="Amazon", nav="Amazon", type="integration"),
    dict(url="/integrations/advertising/", title="Advertising", nav="Advertising", type="hub"),
    dict(url="/integrations/advertising/meta-ads/", title="Meta Ads", nav="Meta Ads", type="integration"),
    dict(url="/integrations/advertising/google-ads/", title="Google Ads", nav="Google Ads", type="integration"),
    dict(url="/integrations/analytics/", title="Web analytics and search", nav="Analytics", type="hub"),
    dict(url="/integrations/analytics/google-analytics-4/", title="Google Analytics 4", nav="Google Analytics 4", type="integration"),
    dict(url="/integrations/analytics/google-search-console/", title="Google Search Console", nav="Search Console", type="integration"),
    dict(url="/integrations/finance/", title="Payments and accounting", nav="Finance", type="hub"),
    dict(url="/integrations/finance/stripe/", title="Stripe", nav="Stripe", type="integration"),
    dict(url="/integrations/finance/xero/", title="Xero", nav="Xero", type="integration"),
    dict(url="/integrations/finance/quickbooks/", title="QuickBooks", nav="QuickBooks", type="integration"),
    dict(url="/integrations/subscriptions/recharge/", title="Recharge (subscriptions)", nav="Recharge", type="integration"),
    dict(url="/integrations/subscriptions/", title="Subscriptions", nav="Subscriptions", type="hub"),
    dict(url="/integrations/workspace/", title="Workspace and documents", nav="Workspace", type="hub"),
    dict(url="/integrations/workspace/slack/", title="Slack", nav="Slack", type="integration"),
    dict(url="/integrations/workspace/documents/", title="Documents and files", nav="Documents", type="integration"),
    dict(url="/integrations/custom/", title="Custom connectors and ERPs", nav="Custom connectors", type="integration"),
    # Solutions
    dict(url="/solutions/", title="Solutions by buyer", nav="Solutions", type="hub"),
    dict(url="/solutions/founders/", title="For founders and CEOs of Shopify brands", nav="Founders and CEOs", type="solution"),
    dict(url="/solutions/subscription-brands/", title="For subscription DTC brands", nav="Subscription brands", type="solution"),
    dict(url="/solutions/finance-leads/", title="For CFOs and finance leads", nav="Finance leads", type="solution"),
    dict(url="/solutions/growth-teams/", title="For growth and marketing teams", nav="Growth teams", type="solution"),
    dict(url="/solutions/shopify-and-amazon-sellers/", title="For Shopify and Amazon sellers", nav="Shopify + Amazon", type="solution"),
    dict(url="/solutions/european-brands/", title="For European and UK brands", nav="European brands", type="solution"),
    dict(url="/solutions/mastercard-business-bonus/", title="For Mastercard Business Bonus merchants", nav="Mastercard Business Bonus", type="solution"),
    # Pricing
    dict(url="/pricing/", title="Pricing model", nav="Pricing", type="pricing"),
    dict(url="/pricing/trial-and-signup/", title="Trial and signup", nav="Trial and signup", type="pricing"),
    # Security
    dict(url="/security/", title="Security and data handling", nav="Security", type="security"),
    dict(url="/security/data-handling/", title="How Luca stores and processes your data", nav="Data handling", type="security"),
    dict(url="/security/access-and-scopes/", title="Access, scopes and deletion", nav="Access and deletion", type="security"),
    # Support and company
    dict(url="/support/", title="Onboarding, services and support", nav="Onboarding and support", type="support"),
    dict(url="/support/onboarding/", title="Onboarding: done with you", nav="Onboarding", type="support"),
    dict(url="/support/community/", title="Community and podcast", nav="Community", type="support"),
    dict(url="/about/", title="About Luca", nav="About", type="support"),
    dict(url="/customers/", title="Customers and proof", nav="Customers", type="support"),
    # Review
    dict(url="/review/", title="Documentation coverage and open questions", nav="Coverage and open questions", type="review"),
]

# ---------------------------------------------------------------------------
# Documented parameters. Inventory IDs keep their inventory weight / status columns
# (pulled from the inventory CSV by build.py). M-IDs are Luca microfeatures not in the inventory.
#   facts: (statement, source-key). Writers may use ONLY these facts.
# ---------------------------------------------------------------------------
P = []
def add(id, dest, status, facts, name=None, scope=None, related=()):
    P.append(dict(id=id, dest=dest, status=status, facts=facts, name=name, scope=scope, related=list(related)))

# ---- Integrations
add("U1", "/integrations/commerce/shopify/", "available", [
    ("Shopify appears as a connected source in Luca's Connect & Setup screen, with connection states Connected, Completed and Syncing.", "deck"),
    ("The website tells new users to start with Shopify or Amazon, then add advertising, analytics and finance sources.", "site"),
    ("Shopify data was reconciled with subscription and accounting data into Numbers for a live client.", "c1002"),
], name="Shopify connector")
add("U2", "/integrations/commerce/amazon/", "available", [
    ("Amazon is listed as a data connection in Luca's product walkthrough.", "c1002"),
    ("The website names Amazon, alongside Shopify, as a starting source.", "site"),
], name="Amazon connector")
add("U6", "/integrations/advertising/meta-ads/", "available", [
    ("Meta / Facebook Ads appears as connected in the Connect & Setup screen.", "deck"),
], name="Meta Ads connector")
add("U7", "/integrations/advertising/google-ads/", "available", [
    ("Google Ads appears as connected in the Connect & Setup screen.", "deck"),
    ("Luca's privacy policy states that Luca's access to Google accounts is read-only and that Luca does not write to, change or delete anything in your Google accounts.", "privacy"),
], name="Google Ads connector")
add("U10", "/integrations/analytics/google-analytics-4/", "available", [
    ("Google Analytics is part of the data Eric described Luca reasoning across.", "c0717"),
    ("Google Analytics is listed as a data connection in the product walkthrough.", "c1002"),
    ("Google data is handled under Google's API Limited Use policy and is deleted within 30 days of disconnecting.", "privacy"),
], name="Google Analytics 4 connector")
add("U11", "/integrations/analytics/google-search-console/", "available", [
    ("The privacy policy names Google Search Console access with the read-only webmasters.readonly scope.", "privacy"),
    ("Search Console is connected in Luca's own internal workspace.", "ecc"),
], name="Google Search Console connector")
add("U15", "/integrations/finance/stripe/", "available", [
    ("Stripe appears in the Connect & Setup screen.", "deck"),
    ("Stripe is listed as a data connection in the product walkthrough.", "c1002"),
], name="Stripe connector")
add("U17", "/integrations/finance/xero/", "available", [
    ("Xero appears as connected in the Connect & Setup screen.", "deck"),
    ("For a subscription client, accounting data was reconciled with Shopify and Recharge data into one database.", "c1002"),
], name="Xero connector")
add("U18", "/integrations/finance/quickbooks/", "scoped", [
    ("Eric described the accounting connection as covering QuickBooks as well as Xero.", "henrik"),
    ("A live subscription client's stack was described as Shopify, Recharge, Meta and QuickBooks or Xero.", "c1002"),
], name="QuickBooks connector",
   scope="Stated by Luca's founder; QuickBooks does not appear in the product screenshot we hold. Confirm the connection during setup.")
add("U14", "/integrations/subscriptions/recharge/", "scoped", [
    ("Recharge subscription data was connected and reconciled with Shopify and accounting data into one clean database for a live subscription client.", "c1002"),
    ("That client's pain, in their words relayed by Eric: Shopify does not talk to Recharge, and Recharge does not talk to the accounting platform.", "c1002"),
], name="Recharge subscription data",
   scope="Connected and reconciled by Luca's team as part of a Numbers build, not a self-serve connector button.")
add("U94", "/integrations/workspace/slack/", "available", [
    ("Luca's product includes an 'Add Luca to Slack' option with an integration guide.", "deck"),
    ("The guide covers installing the Slack app, sending Luca a direct message and mentioning Luca in a channel.", "deck"),
], name="Slack app")
add("U192", "/integrations/workspace/slack/", "available", [
    ("Users can work with Luca from Slack by direct message or by mentioning Luca in a channel.", "deck"),
], name="Answers delivered in Slack")
add("U27", "/integrations/workspace/documents/", "available", [
    ("Luca's product includes 'Upload company docs' and 'Manage Knowledge Base'.", "deck"),
    ("Eric described adding context from documents such as PDFs or emails.", "henrik"),
], name="Upload documents and files as context")
add("U22", "/integrations/custom/", "scoped", [
    ("For systems without a standard connector, such as a custom ERP, Luca's team builds the API connection; Eric put the time at a couple of days.", "henrik"),
    ("The pricing page says custom connections are not a self-serve button yet and are arranged with the team.", "pricing"),
], name="Custom ERP and internal-system connections",
   scope="Built by Luca's team on request. Timing and scope are agreed per account.")
add("U28", "/integrations/custom/", "scoped", [
    ("The website states that custom connectors are built at no integration fee.", "site"),
    ("Custom work is done by Luca's team, not self-serve.", "pricing"),
], name="Custom connectors built by Luca's team, no integration fee",
   scope="Delivered by Luca's team; lead time is agreed per request.")
add("U31", "/products/features/data-connection/", "available", [
    ("Standard sources connect through each platform's own sign-in and permission screen; the pricing page describes it as two clicks per source for most users.", "pricing"),
    ("New users connect a data source during signup.", "c0925"),
], name="Connect a source in two clicks (OAuth)")

# ---- Luca agent
add("U84", "/products/luca-agent/", "available", [
    ("Luca is used through a chat interface ('Luca Web Chat') over the user's connected data.", "deck"),
    ("Organic users connect a data source and start chatting with Luca.", "c0605"),
    ("A September 2026 third-party round-up (Rivo) describes Luca as suited to cross-functional analysis across commerce, marketing, finance, inventory and cash flow.", "rivo"),
], name="Ask questions in plain English across connected sources")
add("U85", "/products/luca-agent/", "scoped", [
    ("Luca's design is one main orchestrator with tools beneath it, reasoning across the business's sources rather than one tool at a time.", "c0522"),
    ("The problem Luca is positioned against, accepted by Eric: data is fragmented and there is no coherent reasoning layer across tools.", "c0717"),
], name="Answers that combine marketing, finance and commerce data",
   scope="Answers can only span the sources the account has connected and that Luca's team has reconciled.")
add("U86", "/products/luca-agent/", "available", [
    ("Luca generates charts and graphs on the fly in answer to a question, rather than from a fixed set of dashboards.", "ecc"),
], name="Charts generated from a question")
add("U87", "/products/luca-agent/", "available", [
    ("Luca is used as an ongoing conversation; Eric reported users returning four to five times a day.", "c0724"),
], name="Follow-up questions in the same conversation")
add("U92", "/products/luca-agent/", "available", [
    ("The pricing page lists unlimited usage on every plan, with no question or credit limit.", "pricing"),
], name="Unlimited questions, no AI credits")
add("U93", "/products/luca-agent/", "available", [
    ("Luca runs as a web application at app.ask-luca.com.", "site"),
], name="Web app")
add("U119", "/products/luca-agent/", "available", [
    ("Luca produces recommendations and step-by-step plans, not only numbers.", "ecc"),
    ("Luca is done-with-you: it does the analysis and proposes the strategy; the operator validates and executes.", "c0724"),
], name="Recommended next steps")
add("U103", "/products/luca-agent/", "scoped", [
    ("Content generation (posts, newsletters, images and brand assets) is listed in Luca's product walkthrough.", "c1002"),
], name="Marketing content drafting",
   scope="A secondary capability; output is a draft for the team to review.")
add("U127", "/products/luca-agent/", "available", [
    ("Luca is done-with-you, not done-for-you: Luca does the analysis and strategy and the operator validates and executes.", "c0724"),
    ("Luca's team works alongside clients during onboarding and data reconciliation.", "c0925"),
], name="Done-with-you analysis and strategy")
add("M1", "/products/luca-agent/", "available", [
    ("When asked to automate a change in Shopify or Meta, Luca replied that it could not, offered to explain how to do it, and said a human stays in the loop.", "c0724"),
], name="Tells you plainly when a request is outside what it does",
   related=["/products/features/control-and-safety/"])

# ---- Numbers
add("U32", "/products/numbers/", "available", [
    ("Numbers reconciles a client's Shopify, subscription and accounting data into one clean database and shows it as a unified view.", "c1002"),
    ("Eric: 'we're rolling this out for several clients now' and it 'becomes table stake… for every client.'", "c1002"),
], name="One reconciled database across your sources")
add("U189", "/products/numbers/", "available", [
    ("Numbers is a control centre to run the business, shown above the chat.", "c1002"),
    ("Eric: the dashboard is the reconciled data — 'there's nothing AI into this' — and Luca sits on top of it.", "c1002"),
], name="Unified control-centre view")
add("U50", "/products/numbers/", "available", [
    ("Net revenue is part of the reconciled commerce view.", "site"),
], name="Net revenue")
add("U67", "/products/numbers/", "available", [
    ("Cohort visibility was built for a live subscription client who previously had 'zero visibility on the cohorts'.", "c1002"),
], name="Cohort analysis")
add("U69", "/products/numbers/", "scoped", [
    ("The same client could not tell active from inactive customers before Numbers; the reconciled view addressed it.", "c1002"),
], name="Active vs lapsed customers",
   scope="Built for a subscription client's reconciled data; confirm for your data model.")
add("U180", "/products/numbers/", "scoped", [
    ("Luca rebuilt a client's historical subscription-skip data from several systems and found a previously unknown $72,000 revenue shortfall.", "news"),
], name="Subscription skips, pauses and gaps",
   scope="Delivered through a reconciliation project by Luca's team.")
add("U34", "/products/numbers/", "scoped", [
    ("For the first Numbers client, reconciling Shopify, Recharge and accounting data took about three weeks of work by Luca's team.", "c1002"),
], name="Reconciled with accounting data",
   scope="A reconciliation project led by Luca's team, not an instant connector result.")
add("M2", "/products/numbers/", "available", [
    ("Numbers shows Shopify, Amazon, Google Analytics and Stripe connections in the demonstrated build.", "c1002"),
], name="Data connections shown on Numbers")

# ---- Knowledge base
add("U146", "/products/knowledge-base/", "available", [
    ("Users can upload company documents and manage a knowledge base in the product.", "deck"),
], name="Upload company documents to a knowledge base")
add("U147", "/products/knowledge-base/", "scoped", [
    ("The website lists goals, constraints, cost rules, lead times and seasonality as the context the knowledge base holds.", "site"),
    ("Context can come from documents such as PDFs or emails.", "henrik"),
], name="Goals, constraints and cost rules as context",
   scope="Luca uses what the account uploads; confirm how each type of context is applied.")
add("M3", "/products/knowledge-base/", "available", [
    ("Luca's own internal knowledge base, written by its team as skills, makes Luca aware of what it can and cannot do.", "c1002"),
], name="Built-in knowledge of its own capabilities")

# ---- Capital
add("U178", "/products/capital/", "available", [
    ("Capital is a feature that Luca's intelligence can unlock, not a parallel product and not a requirement for using Luca.", "positioning"),
    ("Eric deliberately does not lead with capital, to avoid attracting funding seekers instead of operators.", "c0807"),
], name="Capital is optional")
add("U179", "/products/capital/", "available", [
    ("Eric's canonical statement: 'We are not a financing company. We are an Agentic AI company for e-commerce.'", "positioning"),
    ("The website states that any capital is provided through lending partners.", "site"),
], name="Luca is not a lender")

# ---- Features: control and safety
add("U137", "/products/features/control-and-safety/", "available", [
    ("Nothing changes in a connected system without the user: Luca suggests, and a human stays in the loop.", "c0724"),
    ("The website states that every action needs approval by default.", "site"),
], name="Nothing changes without your approval")
add("U144", "/products/features/control-and-safety/", "available", [
    ("Luca is agent-readable, not agent-writable: it reads connected data, gets context and reasons. Eric will not make it write to live systems without strong guardrails and audit trails.", "c0522"),
    ("The privacy policy states Luca's Google access is read-only.", "privacy"),
], name="Read-only by design")

# ---- Features: teams, seats, regions
add("U196", "/products/features/teams-and-seats/", "available", [
    ("Plans are sold by seat: one seat, three seats, or unlimited seats.", "pricing"),
], name="Seats per plan")
add("U197", "/products/features/teams-and-seats/", "available", [
    ("The largest plan includes unlimited seats with full and standard access levels.", "pricing"),
], name="Unlimited-seat option")
add("U187", "/products/features/teams-and-seats/", "available", [
    ("Pricing is published in GBP, USD, EUR and AUD.", "pricing"),
    ("Luca operates from London and Luxembourg and serves brands in Europe, the UK, the US and Australia.", "about"),
], name="Serves brands across the UK, EU, US and Australia")

# ---- Security
add("U213", "/security/data-handling/", "available", [
    ("Each customer's data sits in a separate BigQuery dataset on Google Cloud Platform; credentials are kept in Google Secret Manager.", "privacy"),
], name="Customer data kept separate")
add("U214", "/security/data-handling/", "available", [
    ("The language model provider (OpenAI) processes data under enterprise terms that exclude training on it.", "privacy"),
    ("The website states that Luca does not train third-party foundation models on customers' financials.", "site"),
], name="Your data is not used to train AI models")
add("U216", "/security/data-handling/", "available", [
    ("The privacy policy names OpenAI and Google Cloud Platform as sub-processors.", "privacy"),
], name="Sub-processors disclosed")
add("U218", "/security/access-and-scopes/", "available", [
    ("Google data is deleted within 30 days of disconnecting.", "privacy"),
    ("The privacy policy states how long other data is retained after an account closes.", "privacy"),
], name="Deletion and retention after you disconnect")
add("U219", "/security/access-and-scopes/", "scoped", [
    ("The privacy policy names the read-only Search Console scope (webmasters.readonly) and states Google access is read-only.", "privacy"),
], name="Read-only access scopes",
   scope="Published for Google connections; scopes for other connectors are shown on each platform's own permission screen.")
add("M4", "/security/data-handling/", "available", [
    ("Infrastructure runs on Google Cloud Platform.", "privacy"),
], name="Hosted on Google Cloud Platform")

# ---- Pricing
add("CO1", "/pricing/", "available", [
    ("Plans and prices are published on ask-luca.com/pricing without a sales call.", "pricing"),
], name="Published pricing")
add("CO4", "/pricing/", "available", [
    ("Luca prices by seat, not by store revenue, orders or ad spend.", "pricing"),
], name="Priced by seat")
add("CO5", "/pricing/", "available", [
    ("Because pricing is per seat, the plan price does not rise as the brand's revenue or order volume grows.", "pricing"),
], name="Price does not rise with your revenue")
add("CO6", "/pricing/", "available", [
    ("Every plan lists unlimited usage.", "pricing"),
], name="Unlimited usage on every plan")
add("CO15", "/pricing/", "available", [
    ("The website states custom connectors carry no integration fee.", "site"),
], name="No integration fees")
add("CO17", "/pricing/", "available", [
    ("Luca is positioned as doing the work of an analyst and advisor for a growing brand that cannot yet hire one.", "site"),
], name="Compared with hiring an analyst")
add("CO11", "/pricing/", "available", [
    ("Annual billing is offered at a discount to monthly.", "pricing"),
], name="Annual billing discount")
add("CO9", "/pricing/trial-and-signup/", "available", [
    ("Signup asks for a data connection and card details up front.", "c0925"),
], name="Card and data connection at signup")
add("CO16", "/solutions/mastercard-business-bonus/", "available", [
    ("Luca has a dedicated pricing page for Mastercard Business Bonus.", "pricing"),
    ("Luca is listed on Mastercard's Business Bonus page.", "mc"),
], name="Mastercard Business Bonus partner pricing")
add("M5", "/pricing/trial-and-signup/", "available", [
    ("Signup includes creating an organisation before connecting data.", "c0904"),
], name="Organisation setup during signup")

# ---- Support, community, company
add("S3", "/support/onboarding/", "available", [
    ("Onboarding is hands-on: Luca's team does significant onboarding work for each client; Eric called it 'incredibly labour intensive on our side'.", "c0925"),
    ("Onboarding capacity is managed by intake; October 2026 intake filled after 17–18 outbound signings in September.", "c0925"),
], name="Hands-on onboarding with Luca's team")
add("S4", "/support/onboarding/", "available", [
    ("Luca's team handles custom connectors and integration mapping.", "site"),
    ("The team reconciles a client's systems into Numbers.", "c1002"),
], name="Data mapping done by Luca's team")
add("S10", "/support/community/", "available", [
    ("Luca runs a community for clients and prospects on Heartbeat (community.ask-luca.com, plus iOS and Android apps) to exchange prompts, workflows and use cases.", "community"),
], name="Luca community")
add("T18", "/support/community/", "available", [
    ("Eric hosts the E-Commerce Leaders Series podcast with e-commerce operators.", "ecc"),
], name="E-Commerce Leaders Series podcast")
add("T14", "/about/", "available", [
    ("Eric Bidinger, co-founder and CEO: aerospace engineer with 17 years in private equity.", "about"),
], name="Founder background")
add("R9", "/about/", "available", [
    ("The about page names the team: Eric Bidinger (CEO), Abbas Khaku (COO), Ciske Smit (Head of Product), Kaan Simsek (Head of Data), and engineers Hassaan Mirza and Usman Jameel.", "about"),
], name="Team")
add("R5", "/about/", "available", [
    ("OpenAI is named as the language-model sub-processor.", "privacy"),
], name="AI model provider disclosed")
add("R6", "/about/", "available", [
    ("Numbers moved from a first client build to every client between September and October 2026.", "c1002"),
], name="Product velocity")
add("T8", "/customers/", "available", [
    ("Customer logos shown on ask-luca.com: Untamed, Circus, Prim, Twigs, Nidra, David Gandy Wellwear, Fabulous and Ayodi.", "site"),
], name="Customer logos")
add("T9", "/customers/", "available", [
    ("Named testimonials with photographs are published on ask-luca.com from leaders at Ayodi, Untamed and Nidra.", "site"),
], name="Named testimonials")

# ---- Solutions (buyer sets, certain rows only)
FD = "/solutions/founders/"
add("FD1", FD, "available", [("Numbers gives one reconciled view of the business.", "c1002")])
add("FD2", FD, "available", [("Questions are asked in plain English over connected data, with charts generated on the fly.", "ecc")])
add("FD10", FD, "available", [("Luca is positioned as the analyst a growing brand cannot yet hire.", "site")])
add("FD11", FD, "available", [("A human stays in the loop; Luca does not change connected systems on its own.", "c0724")])
add("FD17", FD, "available", [("Customer data is not used to train AI models.", "privacy")])
add("FD18", FD, "available", [("New users connect their own data during signup and work on it from the first session.", "c0925")])
add("FD20", FD, "available", [("Luca reasons over Shopify together with ads, analytics, payments and accounting data; the website contrasts this with Shopify Sidekick, which works inside Shopify.", "site")])
add("FD21", FD, "available", [("Connected sources stay connected and context is held in a knowledge base, instead of exporting files to a general chatbot each time.", "deck")])
add("FD29", FD, "available", [("Luca is used as a conversation with an analyst, not a dashboard.", "ecc")])
add("FD30", FD, "available", [("Luca's team onboards each client directly.", "c0925")])
SU = "/solutions/subscription-brands/"
add("SU2", SU, "available", [("For a subscription client, Shopify, Recharge and accounting data were reconciled into one view.", "c1002")])
add("SU3", SU, "available", [("Active versus inactive subscribers became visible after reconciliation.", "c1002")])
add("SU4", SU, "available", [("Rebuilt subscription-skip history revealed a $72,000 revenue shortfall for one client.", "news")])
add("SU6", SU, "available", [("Cohort visibility was the stated gap Numbers closed.", "c1002")])
add("SU1", SU, "scoped", [("Recharge data was connected for a live client.", "c1002")], scope="Set up by Luca's team.")
CF = "/solutions/finance-leads/"
add("CF18", CF, "available", [("Luca does not move money or change systems; a human stays in the loop.", "c0724")])
add("CF22", CF, "available", [("Luca reads accounting data alongside commerce data; the accounting system remains the ledger.", "c1002")])
add("CF25", CF, "available", [("Retention and deletion terms are set out in the privacy policy, including 30-day deletion of Google data after disconnecting.", "privacy")])
add("CF1", CF, "scoped", [("For the first Numbers client, accounting, Shopify and Recharge data were reconciled by Luca's team over about three weeks.", "c1002")], scope="A reconciliation project, confirmed per account.")
add("CF2", CF, "scoped", [("Xero is connected in the product; QuickBooks is stated by the founder.", "deck")], scope="Xero confirmed; QuickBooks to confirm during setup.")
GR = "/solutions/growth-teams/"
add("GR21", GR, "available", [("Teams can use Luca from Slack by direct message or channel mention.", "deck")])
add("GR23", GR, "available", [("Google Analytics and Search Console connect alongside ad platforms.", "privacy")])
MC = "/solutions/shopify-and-amazon-sellers/"
add("MC1", MC, "scoped", [("Shopify and Amazon both connect as commerce sources.", "c1002")], scope="Both sources connect; how they are combined in reporting is confirmed per account.")
EU = "/solutions/european-brands/"
add("EU4", EU, "available", [("Pricing is published in EUR and GBP as well as USD and AUD.", "pricing")])
add("EU12", EU, "available", [("A Mastercard Business Bonus pricing page exists, and Luca is listed on Mastercard's Business Bonus page.", "mc")])
add("EU3", EU, "scoped", [("Xero is connected in the product.", "deck")], scope="Xero confirmed; other European accounting and banking sources to confirm.")
MB = "/solutions/mastercard-business-bonus/"
add("MB1", MB, "available", [("A dedicated Mastercard Business Bonus pricing page exists on ask-luca.com.", "pricing")])
add("MB2", MB, "available", [("The partner page offers a discount on every plan, monthly and annual.", "pricing")])
add("MB4", MB, "available", [("Luca is listed on Mastercard's Business Bonus page beside large consumer brands.", "mc")])
add("MB6", MB, "available", [("The partner discount applies to the same plans as standard pricing.", "pricing")])
add("SC8", "/products/features/teams-and-seats/", "available", [("Unlimited seats are available on the largest plan.", "pricing")])
