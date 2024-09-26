Digital and In-street Activism Events

# Goal of this project

## Identify the protest events against public firms in the United States covered by major online and traditional media from 2008 to 2019

## Classify these events into in-street, digital spectator, digital transitional, and digital gladiatorial activities

    Digital activism is a tactic that is defined as activists using digital technologies to present their requests, whereas, in-street activism is a tactic that is defined as activists physically present on the street. 
    
    George and Leidner (2019) have classified digital activism into three types based on their degree of impact:
    
    ## Digital spectator activities
    
    Clicktivism, Metavoicing, Assertion
    
    ## Digital transitional activities
    
    Political consumerism
    Digital petitions
    Botivism
    E-funding
    
    
    ## Digital gladiatorial activities
    
    Data activism
    Exposure
    Hacktivism

    One event can be classified into several categories

## Document the article source and text for check

The flow chat is as follows

```mermaid

graph TD
    A[Collect protests event against public firms from LexisNexis, Proquest, GDELT Project, RavenPack and Factiva] --> B{Public firms and protest-related keywords are both mentioned in the news/time period between 2008 and 2019}
    B -->|Yes| I[Keep in dataset] --> C{Firms is the target of the protest}
    B -->|No| 
    C --> |Yes| J[Keep in dataset]
    C -->|No| 
    C--> D1{Is it physically present on the street}
    D1 -->|Yes| E[Label as in-street protests]
    D1 -->|No|
    C--> D2{Does it include spectator activities}
    D2 -->|Yes| F[Label as digital spectator protests]
    D2 -->|No|
    C --> D3{Does it inlclude transitional activities}
    D3 -->|Yes| G[Label as digital spectator protests]
    D3 -->|No|
    C --> D4{Does it inlclude gladiatorial activities}
    D4 -->|Yes| H[Label as digital spectator protests]
    D4 -->|No|

```

# Citations
George, Jordana J., and Dorothy E. Leidner. "From clicktivism to hacktivism: Understanding digital activism." Information and organization 29.3 (2019): 100249


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


