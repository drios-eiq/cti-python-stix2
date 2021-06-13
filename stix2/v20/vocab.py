"""
STIX 2.0 open vocabularies and enums
"""

ATTACK_MOTIVATION_ACCIDENTAL = "accidental"
ATTACK_MOTIVATION_COERCION = "coercion"
ATTACK_MOTIVATION_DOMINANCE = "dominance"
ATTACK_MOTIVATION_IDEOLOGY = "ideology"
ATTACK_MOTIVATION_NOTORIETY = "notoriety"
ATTACK_MOTIVATION_ORGANIZATIONAL_GAIN = "organizational-gain"
ATTACK_MOTIVATION_PERSONAL_GAIN = "personal-gain"
ATTACK_MOTIVATION_PERSONAL_SATISFACTION = "personal-satisfaction"
ATTACK_MOTIVATION_REVENGE = "revenge"
ATTACK_MOTIVATION_UNPREDICTABLE = "unpredictable"


ATTACK_MOTIVATION = [
    ATTACK_MOTIVATION_ACCIDENTAL,
    ATTACK_MOTIVATION_COERCION,
    ATTACK_MOTIVATION_DOMINANCE,
    ATTACK_MOTIVATION_IDEOLOGY,
    ATTACK_MOTIVATION_NOTORIETY,
    ATTACK_MOTIVATION_ORGANIZATIONAL_GAIN,
    ATTACK_MOTIVATION_PERSONAL_GAIN,
    ATTACK_MOTIVATION_PERSONAL_SATISFACTION,
    ATTACK_MOTIVATION_REVENGE,
    ATTACK_MOTIVATION_UNPREDICTABLE,
]


ATTACK_RESOURCE_LEVEL_INDIVIDUAL = "individual"
ATTACK_RESOURCE_LEVEL_CLUB = "club"
ATTACK_RESOURCE_LEVEL_CONTEST = "contest"
ATTACK_RESOURCE_LEVEL_TEAM = "team"
ATTACK_RESOURCE_LEVEL_ORGANIZATION = "organization"
ATTACK_RESOURCE_LEVEL_GOVERNMENT = "government"


ATTACK_RESOURCE_LEVEL = [
    ATTACK_RESOURCE_LEVEL_INDIVIDUAL,
    ATTACK_RESOURCE_LEVEL_CLUB,
    ATTACK_RESOURCE_LEVEL_CONTEST,
    ATTACK_RESOURCE_LEVEL_TEAM,
    ATTACK_RESOURCE_LEVEL_ORGANIZATION,
    ATTACK_RESOURCE_LEVEL_GOVERNMENT,
]


HASHING_ALGORITHM_MD5 = "MD5"
HASHING_ALGORITHM_MD6 = "MD6"
HASHING_ALGORITHM_RIPEMD_160 = "RIPEMD-160"
HASHING_ALGORITHM_SHA_1 = "SHA-1"
HASHING_ALGORITHM_SHA_224 = "SHA-224"
HASHING_ALGORITHM_SHA_256 = "SHA-256"
HASHING_ALGORITHM_SHA_384 = "SHA-384"
HASHING_ALGORITHM_SHA_512 = "SHA-512"
HASHING_ALGORITHM_SHA3_224 = "SHA3-224"
HASHING_ALGORITHM_SHA3_256 = "SHA3-256"
HASHING_ALGORITHM_SHA3_384 = "SHA3-384"
HASHING_ALGORITHM_SHA3_512 = "SHA3-512"
HASHING_ALGORITHM_SSDEEP = "ssdeep"
HASHING_ALGORITHM_WHIRLPOOL = "WHIRLPOOL"


HASHING_ALGORITHM = [
    HASHING_ALGORITHM_MD5,
    HASHING_ALGORITHM_MD6,
    HASHING_ALGORITHM_RIPEMD_160,
    HASHING_ALGORITHM_SHA_1,
    HASHING_ALGORITHM_SHA_224,
    HASHING_ALGORITHM_SHA_256,
    HASHING_ALGORITHM_SHA_384,
    HASHING_ALGORITHM_SHA_512,
    HASHING_ALGORITHM_SHA3_224,
    HASHING_ALGORITHM_SHA3_256,
    HASHING_ALGORITHM_SHA3_384,
    HASHING_ALGORITHM_SHA3_512,
    HASHING_ALGORITHM_SSDEEP,
    HASHING_ALGORITHM_WHIRLPOOL,
]


IDENTITY_CLASS_INDIVIDUAL = "individual"
IDENTITY_CLASS_GROUP = "group"
IDENTITY_CLASS_ORGANIZATION = "organization"
IDENTITY_CLASS_CLASS = "class"
IDENTITY_CLASS_UNKNOWN = "unknown"


IDENTITY_CLASS = [
    IDENTITY_CLASS_INDIVIDUAL,
    IDENTITY_CLASS_GROUP,
    IDENTITY_CLASS_ORGANIZATION,
    IDENTITY_CLASS_CLASS,
    IDENTITY_CLASS_UNKNOWN,
]


INDICATOR_LABEL_ANOMALOUS_ACTIVITY = "anomalous-activity"
INDICATOR_LABEL_ANONYMIZATION = "anonymization"
INDICATOR_LABEL_BENIGN = "benign"
INDICATOR_LABEL_COMPROMISED = "compromised"
INDICATOR_LABEL_MALICIOUS_ACTIVITY = "malicious-activity"
INDICATOR_LABEL_ATTRIBUTION = "attribution"


INDICATOR_LABEL = [
    INDICATOR_LABEL_ANOMALOUS_ACTIVITY,
    INDICATOR_LABEL_ANONYMIZATION,
    INDICATOR_LABEL_BENIGN,
    INDICATOR_LABEL_COMPROMISED,
    INDICATOR_LABEL_MALICIOUS_ACTIVITY,
    INDICATOR_LABEL_ATTRIBUTION,
]


INDUSTRY_SECTOR_AGRICULTURE = "agriculture"
INDUSTRY_SECTOR_AEROSPACE = "aerospace"
INDUSTRY_SECTOR_AUTOMOTIVE = "automotive"
INDUSTRY_SECTOR_COMMUNICATIONS = "communications"
INDUSTRY_SECTOR_CONSTRUCTION = "construction"
INDUSTRY_SECTOR_DEFENCE = "defence"
INDUSTRY_SECTOR_EDUCATION = "education"
INDUSTRY_SECTOR_ENERGY = "energy"
INDUSTRY_SECTOR_ENTERTAINMENT = "entertainment"
INDUSTRY_SECTOR_FINANCIAL_SERVICES = "financial-services"
INDUSTRY_SECTOR_GOVERNMENT_NATIONAL = "government-national"
INDUSTRY_SECTOR_GOVERNMENT_REGIONAL = "government-regional"
INDUSTRY_SECTOR_GOVERNMENT_LOCAL = "government-local"
INDUSTRY_SECTOR_GOVERNMENT_PUBLIC_SERVICES = "government-public-services"
INDUSTRY_SECTOR_HEALTHCARE = "healthcare"
INDUSTRY_SECTOR_HOSPITALITY_LEISURE = "hospitality-leisure"
INDUSTRY_SECTOR_INFRASTRUCTURE = "infrastructure"
INDUSTRY_SECTOR_INSURANCE = "insurance"
INDUSTRY_SECTOR_MANUFACTURING = "manufacturing"
INDUSTRY_SECTOR_MINING = "mining"
INDUSTRY_SECTOR_NON_PROFIT = "non-profit"
INDUSTRY_SECTOR_PHARMACEUTICALS = "pharmaceuticals"
INDUSTRY_SECTOR_RETAIL = "retail"
INDUSTRY_SECTOR_TECHNOLOGY = "technology"
INDUSTRY_SECTOR_TELECOMMUNICATIONS = "telecommunications"
INDUSTRY_SECTOR_TRANSPORTATION = "transportation"
INDUSTRY_SECTOR_UTILITIES = "utilities"


INDUSTRY_SECTOR = [
    INDUSTRY_SECTOR_AGRICULTURE,
    INDUSTRY_SECTOR_AEROSPACE,
    INDUSTRY_SECTOR_AUTOMOTIVE,
    INDUSTRY_SECTOR_COMMUNICATIONS,
    INDUSTRY_SECTOR_CONSTRUCTION,
    INDUSTRY_SECTOR_DEFENCE,
    INDUSTRY_SECTOR_EDUCATION,
    INDUSTRY_SECTOR_ENERGY,
    INDUSTRY_SECTOR_ENTERTAINMENT,
    INDUSTRY_SECTOR_FINANCIAL_SERVICES,
    INDUSTRY_SECTOR_GOVERNMENT_NATIONAL,
    INDUSTRY_SECTOR_GOVERNMENT_REGIONAL,
    INDUSTRY_SECTOR_GOVERNMENT_LOCAL,
    INDUSTRY_SECTOR_GOVERNMENT_PUBLIC_SERVICES,
    INDUSTRY_SECTOR_HEALTHCARE,
    INDUSTRY_SECTOR_HOSPITALITY_LEISURE,
    INDUSTRY_SECTOR_INFRASTRUCTURE,
    INDUSTRY_SECTOR_INSURANCE,
    INDUSTRY_SECTOR_MANUFACTURING,
    INDUSTRY_SECTOR_MINING,
    INDUSTRY_SECTOR_NON_PROFIT,
    INDUSTRY_SECTOR_PHARMACEUTICALS,
    INDUSTRY_SECTOR_RETAIL,
    INDUSTRY_SECTOR_TECHNOLOGY,
    INDUSTRY_SECTOR_TELECOMMUNICATIONS,
    INDUSTRY_SECTOR_TRANSPORTATION,
    INDUSTRY_SECTOR_UTILITIES,
]


MALWARE_LABEL_ADWARE = "adware"
MALWARE_LABEL_BACKDOOR = "backdoor"
MALWARE_LABEL_BOT = "bot"
MALWARE_LABEL_DDOS = "ddos"
MALWARE_LABEL_DROPPER = "dropper"
MALWARE_LABEL_EXPLOIT_KIT = "exploit-kit"
MALWARE_LABEL_KEYLOGGER = "keylogger"
MALWARE_LABEL_RANSOMWARE = "ransomware"
MALWARE_LABEL_REMOTE_ACCESS_TROJAN = "remote-access-trojan"
MALWARE_LABEL_RESOURCE_EXPLOITATION = "resource-exploitation"
MALWARE_LABEL_ROGUE_SECURITY_SOFTWARE = "rogue-security-software"
MALWARE_LABEL_ROOTKIT = "rootkit"
MALWARE_LABEL_SCREEN_CAPTURE = "screen-capture"
MALWARE_LABEL_SPYWARE = "spyware"
MALWARE_LABEL_TROJAN = "trojan"
MALWARE_LABEL_VIRUS = "virus"
MALWARE_LABEL_WORM = "worm"


MALWARE_LABEL = [
    MALWARE_LABEL_ADWARE,
    MALWARE_LABEL_BACKDOOR,
    MALWARE_LABEL_BOT,
    MALWARE_LABEL_DDOS,
    MALWARE_LABEL_DROPPER,
    MALWARE_LABEL_EXPLOIT_KIT,
    MALWARE_LABEL_KEYLOGGER,
    MALWARE_LABEL_RANSOMWARE,
    MALWARE_LABEL_REMOTE_ACCESS_TROJAN,
    MALWARE_LABEL_RESOURCE_EXPLOITATION,
    MALWARE_LABEL_ROGUE_SECURITY_SOFTWARE,
    MALWARE_LABEL_ROOTKIT,
    MALWARE_LABEL_SCREEN_CAPTURE,
    MALWARE_LABEL_SPYWARE,
    MALWARE_LABEL_TROJAN,
    MALWARE_LABEL_VIRUS,
    MALWARE_LABEL_WORM,
]


REPORT_LABEL_THREAT_REPORT = "threat-report"
REPORT_LABEL_ATTACK_PATTERN = "attack-pattern"
REPORT_LABEL_CAMPAIGN = "campaign"
REPORT_LABEL_IDENTITY = "identity"
REPORT_LABEL_INDICATOR = "indicator"
REPORT_LABEL_INTRUSION_SET = "intrusion-set"
REPORT_LABEL_MALWARE = "malware"
REPORT_LABEL_OBSERVED_DATA = "observed-data"
REPORT_LABEL_THREAT_ACTOR = "threat-actor"
REPORT_LABEL_TOOL = "tool"
REPORT_LABEL_VULNERABILITY = "vulnerability"


REPORT_LABEL = [
    REPORT_LABEL_THREAT_REPORT,
    REPORT_LABEL_ATTACK_PATTERN,
    REPORT_LABEL_CAMPAIGN,
    REPORT_LABEL_IDENTITY,
    REPORT_LABEL_INDICATOR,
    REPORT_LABEL_INTRUSION_SET,
    REPORT_LABEL_MALWARE,
    REPORT_LABEL_OBSERVED_DATA,
    REPORT_LABEL_THREAT_ACTOR,
    REPORT_LABEL_TOOL,
    REPORT_LABEL_VULNERABILITY,
]


THREAT_ACTOR_LABEL_ACTIVIST = "activist"
THREAT_ACTOR_LABEL_COMPETITOR = "competitor"
THREAT_ACTOR_LABEL_CRIME_SYNDICATE = "crime-syndicate"
THREAT_ACTOR_LABEL_CRIMINAL = "criminal"
THREAT_ACTOR_LABEL_HACKER = "hacker"
THREAT_ACTOR_LABEL_INSIDER_ACCIDENTAL = "insider-accidental"
THREAT_ACTOR_LABEL_INSIDER_DISGRUNTLED = "insider-disgruntled"
THREAT_ACTOR_LABEL_NATION_STATE = "nation-state"
THREAT_ACTOR_LABEL_SENSATIONALIST = "sensationalist"
THREAT_ACTOR_LABEL_SPY = "spy"
THREAT_ACTOR_LABEL_TERRORIST = "terrorist"


THREAT_ACTOR_LABEL = [
    THREAT_ACTOR_LABEL_ACTIVIST,
    THREAT_ACTOR_LABEL_COMPETITOR,
    THREAT_ACTOR_LABEL_CRIME_SYNDICATE,
    THREAT_ACTOR_LABEL_CRIMINAL,
    THREAT_ACTOR_LABEL_HACKER,
    THREAT_ACTOR_LABEL_INSIDER_ACCIDENTAL,
    THREAT_ACTOR_LABEL_INSIDER_DISGRUNTLED,
    THREAT_ACTOR_LABEL_NATION_STATE,
    THREAT_ACTOR_LABEL_SENSATIONALIST,
    THREAT_ACTOR_LABEL_SPY,
    THREAT_ACTOR_LABEL_TERRORIST,
]


THREAT_ACTOR_ROLE_AGENT = "agent"
THREAT_ACTOR_ROLE_DIRECTOR = "director"
THREAT_ACTOR_ROLE_INDEPENDENT = "independent"
THREAT_ACTOR_ROLE_INFRASTRUCTURE_ARCHITECT = "infrastructure-architect"
THREAT_ACTOR_ROLE_INFRASTRUCTURE_OPERATOR = "infrastructure-operator"
THREAT_ACTOR_ROLE_MALWARE_AUTHOR = "malware-author"
THREAT_ACTOR_ROLE_SPONSOR = "sponsor"


THREAT_ACTOR_ROLE = [
    THREAT_ACTOR_ROLE_AGENT,
    THREAT_ACTOR_ROLE_DIRECTOR,
    THREAT_ACTOR_ROLE_INDEPENDENT,
    THREAT_ACTOR_ROLE_INFRASTRUCTURE_ARCHITECT,
    THREAT_ACTOR_ROLE_INFRASTRUCTURE_OPERATOR,
    THREAT_ACTOR_ROLE_MALWARE_AUTHOR,
    THREAT_ACTOR_ROLE_SPONSOR,
]


THREAT_ACTOR_SOPHISTICATION_NONE = "none"
THREAT_ACTOR_SOPHISTICATION_MINIMAL = "minimal"
THREAT_ACTOR_SOPHISTICATION_INTERMEDIATE = "intermediate"
THREAT_ACTOR_SOPHISTICATION_ADVANCED = "advanced"
THREAT_ACTOR_SOPHISTICATION_EXPERT = "expert"
THREAT_ACTOR_SOPHISTICATION_INNOVATOR = "innovator"
THREAT_ACTOR_SOPHISTICATION_STRATEGIC = "strategic"


THREAT_ACTOR_SOPHISTICATION = [
    THREAT_ACTOR_SOPHISTICATION_NONE,
    THREAT_ACTOR_SOPHISTICATION_MINIMAL,
    THREAT_ACTOR_SOPHISTICATION_INTERMEDIATE,
    THREAT_ACTOR_SOPHISTICATION_ADVANCED,
    THREAT_ACTOR_SOPHISTICATION_EXPERT,
    THREAT_ACTOR_SOPHISTICATION_INNOVATOR,
    THREAT_ACTOR_SOPHISTICATION_STRATEGIC,
]


TOOL_LABEL_DENIAL_OF_SERVICE = "denial-of-service"
TOOL_LABEL_EXPLOITATION = "exploitation"
TOOL_LABEL_INFORMATION_GATHERING = "information-gathering"
TOOL_LABEL_NETWORK_CAPTURE = "network-capture"
TOOL_LABEL_CREDENTIAL_EXPLOITATION = "credential-exploitation"
TOOL_LABEL_REMOTE_ACCESS = "remote-access"
TOOL_LABEL_VULNERABILITY_SCANNING = "vulnerability-scanning"


TOOL_LABEL = [
    TOOL_LABEL_DENIAL_OF_SERVICE,
    TOOL_LABEL_EXPLOITATION,
    TOOL_LABEL_INFORMATION_GATHERING,
    TOOL_LABEL_NETWORK_CAPTURE,
    TOOL_LABEL_CREDENTIAL_EXPLOITATION,
    TOOL_LABEL_REMOTE_ACCESS,
    TOOL_LABEL_VULNERABILITY_SCANNING,
]
