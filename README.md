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
    A[Collect protests event] --> B{No duplicated events?}
    B -->|Yes| C[Keep in dataset]
    B -->|No| G[Remove from dataset]
    C --> D{Firms is the target of the protest?}
    D -->|Yes| E[Keep in dataset]
    D -->|No| H[Remove from dataset]
    E --> F1{Is it physically present on the street?}
    F1 -->|Yes| I[Label as in-street protests]
    F1 -->|No| J[Label as other type of protest]

    E--> F2{Does it include spectator activities}
    F2 -->|Yes| K[Label as digital spectator protests]
    F2 -->|No| J[Label as other type of protest]
    E --> F3{Does it inlclude transitional activities}
    F3 -->|Yes| L[Label as digital spectator protests]
    F3 -->|No| J[Label as other type of protest]
    E --> F4{Does it inlclude gladiatorial activities}
    F4 -->|Yes| M[Label as digital spectator protests]
    F4 -->|No| J[Label as other type of protest]

 

```
# Collect protest events

Collect all the news articles with Public firms and protest-related keywords against public firms from LexisNexis, Proquest, GDELT Project, RavenPack and Factiva

Time period between 2008 and 2019

Different websites have different API and keyword searching, so the code for this part is skipped. 

# Collect protest events

BERT_model.py classify the article text based on the criteria from B to F. 
The training set for F1-F4 is stored in training datasets folder. 


# Citations
George, Jordana J., and Dorothy E. Leidner. "From clicktivism to hacktivism: Understanding digital activism." Information and organization 29.3 (2019): 100249




