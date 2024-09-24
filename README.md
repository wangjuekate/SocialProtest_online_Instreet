This is a project that aims to collect social protests against public firms and categorize them into different categories. 

# Define digital activism against firms

Digital activism is a tactic that is defined as activists using digital technologies to present their requests. However, not all the digital activism is critical or matter as it can be effortless just to click or tweet online. When the digital activism capture news media attention means that they exert an impact and should be paid attention to. 

The data verification


```mermaid

graph TD
    A[Identify Digital Activism Campaign] --> B{Media coverage?}
    B -->|Yes| C[Keep in dataset]
    B -->|No| J[Low Priority]
    C --> D[Business related]
    D -->|Yes| E[Keep in dataset]
    D -->|No| F[Low Priority]
    E --> G[Data verification on ]
    F --> G[Consider Longevity and Persistence]
    G --> H[Assess Alignment with Societal Trends]
    H --> I[Monitor Media Coverage]
    I --> K{High Impact Potential?}
    K -->|Yes| L[Prioritize Response]
    K -->|No| M[Monitor and Reassess]

```


## Relevance to business operations:
Digital activism that directly relates to a firm's products, services, practices, or industry is most likely to matter. This could include:


- Campaigns targeting specific company policies
- Industry-wide movements affecting the business environment
- Consumer boycotts or buycotts


## Reach and virality:
Assess the scale and spread of the activist content:


## Number of participants/supporters
Geographic spread
Cross-platform presence
Viral potential


## Stakeholder engagement:
Consider which stakeholders are involved:


Customers
Employees
Investors
Regulators
Media


## Potential business impact:
Assess possible consequences:


## Reputational risks
Financial implications
Regulatory scrutiny
Market share changes


## Longevity and persistence:
Consider the sustainability of the movement:


## One-time event vs. ongoing campaign
Historical context and related movements
Organizational backing


## Alignment with societal trends:
Evaluate how the activism relates to broader social, environmental, or governance issues:


Climate change
Social justice
Corporate responsibility


## Media coverage:
Assess mainstream and social media attention:


# Sources of Data
LexisNexis, ProQuest, RavenPack

# Steps
## Utilize the label from RavenPack

We first collected the news that are 100% related to public firms. 

## Link the news from RavenPack to LexisNexis

Content matching to get the full news. 


## Set up machine learning to categorize the news into needed categories

For example online versus offline


