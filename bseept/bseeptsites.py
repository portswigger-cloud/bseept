#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

import bseeptgraphql
import json

#
# Get the sites configured in the system
#
def getsites(APIURL,APIKEY,doprint=True, output=False):
    
    query = '''
        query GetSiteTree {
            site_tree {
                sites {
                    id
                    name
                    parent_id
                    scope {
                        included_urls
                        excluded_urls
                        protocol_options
                    }
                    scan_configurations{
                        id
                    }
                    application_logins {
                        login_credentials {
                            label
                            username
                        }
                        recorded_logins {
                            label
                        }
                    }
                    ephemeral
                    email_recipients{
                        id
                        email
                    }
                }
            }
        }
        '''

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, None)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result

#
# Get the site tree which is comprised of folders and sites
#
def getsitetree(APIURL,APIKEY, urls=None, parent=1,doprint=True, output=False):
    query = '''
        query GetSiteTree {
            site_tree {
                folders {
                    id
                    name
                    parent_id
                }
                sites {
                    id
                    name
                    parent_id
                    scope {
                        included_urls
                        excluded_urls
                        protocol_options
                    }
                    scan_configurations{
                        id
                    }
                    application_logins {
                        login_credentials {
                            label
                            username
                        }
                        recorded_logins {
                            label
                        }
                    }
                    ephemeral
                    email_recipients{
                        id
                        email
                    }
                }
            }
        }
    '''

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, None)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result


#
# Create a site
#
def createsite(APIURL,APIKEY, name, urls, parent_id, scan_configuration_ids, protocol_options, email_recipients = "", agent_pool_id = "0",print=True, output=False):
 
    #
    #                 $scan_configuration_id: [ID!]           
    # scan_configuration_ids: [$scan_configuration_id]
   #               scan_configuration_ids {
   #                   id
   #              }
    #
    query = '''
    mutation CreateSite($name: String!, $parent_id: ID!, $urls: [String!]!, $protocol_options: ScopeProtocolOptions!, $scan_configuration_ids: [ID!], $agentpoolid: ID!, $email_recipients: [EmailRecipientInput!]) {
 

        create_site(
            input: {
                name: $name
                parent_id: $parent_id
                scope: {
                    included_urls: $urls
                    protocol_options: $protocol_options
                }
                application_logins: {
                    login_credentials: [] 
                    recorded_logins: []
                } 
                scan_configuration_ids: $scan_configuration_ids
                email_recipients: $email_recipients
                agent_pool_id: $agentpoolid
            } 
            ) 
        
        {
            site {
                id
                parent_id
                scope {
                    included_urls
                    protocol_options
                }
                application_logins {
                    login_credentials {
                        id
                        label
                        username
                    }
                    recorded_logins {
                        id
                        label
                    }
                }
                scan_configurations{
                    id
                }
                email_recipients {
                    id
                    email
                }
                agent_pool{
                    id
                    name
                    description
                }
           }
        }
    }'''

    variables = { 
            "name": name, 
            "parent_id": parent_id, 
            "urls": urls, 
            "protocol_options": protocol_options.lstrip('\'').rstrip('\''), 
            "scan_configuration_ids": scan_configuration_ids,
            "email_recipients": email_recipients,
            "agent_pool_id": agent_pool_id
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result


#
# Delete a site
#
def deletesite(APIURL,APIKEY, site_id,print=True, output=False):
 
    query = '''
    mutation DeleteSite($siteid: ID!) {
 
        delete_site(
            input: {
                id: $siteid
            } 
            ) 
        
        {
            id
        }
    }'''

    variables = { 
            "siteid": site_id, 
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result

#
# Rename a site
#
def renamesite(APIURL,APIKEY, site_id, newname,doprint=True, output=False):
 
    query = '''
    mutation RenameSite($siteid: ID!, $name: String!) {
 
        rename_site(
            input: {
                id: $siteid
                name: $name
            } 
        ) 
        
        {
            id
            name
        }
    }'''

    variables = { 
            "siteid": site_id, 
            "name": newname
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result



