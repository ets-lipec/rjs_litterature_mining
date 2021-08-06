class WOSdf:
    # Constructor
    def __init__(self, web_of_science_df):
        self.df = web_of_science_df
        self.pubType = web_of_science_df['Publication Type']
        self.authors = web_of_science_df['Authors']
        self.bookAuthors = web_of_science_df['Book Authors']
        self.bookEditors = web_of_science_df['Book Editors']
        self.bookGroupAuthors = web_of_science_df['Book Group Authors']
        self.authorFullNames = web_of_science_df['Author Full Names']
        self.bookAuthorFullName = web_of_science_df['Book Author Full Names']
        self.groupAuthors = web_of_science_df['Group Authors']
        self.articleTitle = web_of_science_df['Article Title']
        self.sourceTitle = web_of_science_df['Source Title']
        self.bookSeriesTitle = web_of_science_df['Book Series Title']
        self.bookSeriesSubtitle = web_of_science_df['Book Series Subtitle']
        self.language = web_of_science_df['Language']
        self.docType = web_of_science_df['Document Type']
        self.conferenceTitle = web_of_science_df['Conference Title']
        self.conferenceDate = web_of_science_df['Conference Date']
        self.conferenceLocation = web_of_science_df['Conference Location']
        self.conferenceSponsor = web_of_science_df['Conference Sponsor']
        self.conferenceHost = web_of_science_df['Conference Host']
        self.authorKeywords = web_of_science_df['Author Keywords']
        self.keywordsPlus = web_of_science_df['Keywords Plus']
        self.abstract = web_of_science_df['Abstract']
        self.addresses = web_of_science_df['Addresses']
        self.reprintAddresses = web_of_science_df['Reprint Addresses']
        self.emailAddresses = web_of_science_df['Email Addresses']
        self.researcherID = web_of_science_df['Researcher Ids']
        self.orcID = web_of_science_df['ORCIDs']
        self.fundingOrgs = web_of_science_df['Funding Orgs']
        self.fundingText = web_of_science_df['Funding Text']
        self.citedReferences = web_of_science_df['Cited References']
        self.citedReferenceCount = web_of_science_df['Cited Reference Count']
        self.timesCitedWOSCore = web_of_science_df['Times Cited, WoS Core']
        self.timesCitedAllDatabase = web_of_science_df['Times Cited, All Databases']
        self.last180DayUsageCount = web_of_science_df['180 Day Usage Count']
        self.since2013UsageCount = web_of_science_df['Since 2013 Usage Count']
        self.publisher = web_of_science_df['Publisher']
        self.publisherCity = web_of_science_df['Publisher City']
        self.publisherAddress = web_of_science_df['Publisher Address']
        self.issn = web_of_science_df['ISSN']
        self.eissn = web_of_science_df['eISSN']
        self.isbn = web_of_science_df['ISBN']
        self.journalAbbreviation = web_of_science_df['Journal Abbreviation']
        self.journalISOAbbreviation = web_of_science_df['Journal ISO Abbreviation']
        self.publicationDate = web_of_science_df['Publication Date']
        self.publicationYear = web_of_science_df['Publication Year']
        self.volume = web_of_science_df['Volume']
        self.issue = web_of_science_df['Issue']
        self.partNumber = web_of_science_df['Part Number']
        self.supplement = web_of_science_df['Supplement']
        self.specialIssue = web_of_science_df['Special Issue']
        self.meetingAbstract = web_of_science_df['Meeting Abstract']
        self.startPage = web_of_science_df['Start Page']
        self.endPage = web_of_science_df['End Page']
        self.articleNumber = web_of_science_df['Article Number']
        self.doi = web_of_science_df['DOI']
        self.bookDOI = web_of_science_df['Book DOI']
        self.earlyAccesDate = web_of_science_df['Early Access Date']
        self.numberOfPages = web_of_science_df['Number of Pages']
        self.WOSCategories = web_of_science_df['WoS Categories']
        self.researchAreas = web_of_science_df['Research Areas']
        self.IDSNumber = web_of_science_df['IDS Number']
        self.uniqueWOSiD = web_of_science_df['UT (Unique WOS ID)']
        self.pubmedID = web_of_science_df['Pubmed Id']
        self.openAccessDesignations = web_of_science_df['Open Access Designations']
        self.highlyCitedStatus = web_of_science_df['Highly Cited Status']
        self.hotPaperStatus = web_of_science_df['Hot Paper Status']
        self.dateOfExport = web_of_science_df['Date of Export']

import pandas as pd

df_test = pd.read_csv('../WordAnalysis/DataBase_20210522.csv', sep=';')
data = WOSdf(df_test)
print(data.abstract, '\n')
print(data.articleTitle[1])
for col in data.df.columns:
    print(col)
# =============================================================================
# for col in df_test.columns:
#     print(col)
# =============================================================================







'''
'Publication Type'
'Authors'
'Book Authors'
'Book Editors'
'Book Group Authors'
'Author Full Names'
'Book Author Full Names'
'Group Authors'
'Article Title'
'Source Title'
'Book Series Title'
'Book Series Subtitle'
'Language'
'Document Type'
'Conference Title'
'Conference Date'
'Conference Location'
'Conference Sponsor'
'Conference Host'
'Author Keywords'
'Keywords Plus'
'Abstract'
'Addresses'
'Reprint Addresses'
'Email Addresses'
'Researcher Ids'
'ORCIDs'
'Funding Orgs'
'Funding Text'
'Cited References'
'Cited Reference Count'
'Times Cited, WoS Core'
'Times Cited, All Databases'
'180 Day Usage Count'
'Since 2013 Usage Count'
'Publisher'
'Publisher City'
'Publisher Address'
'ISSN'
'eISSN'
'ISBN'
'Journal Abbreviation'
'Journal ISO Abbreviation'
'Publication Date'
'Publication Year'
'Volume'
'Issue'
'Part Number'
'Supplement'
'Special Issue'
'Meeting Abstract'
'Start Page'
'End Page'
'Article Number'
'DOI'
'Book DOI'
'Early Access Date'
'Number of Pages'
'WoS Categories'
'Research Areas'
'IDS Number'
'UT (Unique WOS ID)'
'Pubmed Id'
'Open Access Designations'
'Highly Cited Status'
'Hot Paper Status'
'Date of Export'
'''