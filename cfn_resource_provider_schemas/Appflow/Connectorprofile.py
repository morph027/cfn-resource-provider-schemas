SCHEMA = {
  "typeName" : "AWS::AppFlow::ConnectorProfile",
  "description" : "Resource Type definition for AWS::AppFlow::ConnectorProfile",
  "additionalProperties" : False,
  "properties" : {
    "ConnectorProfileArn" : {
      "description" : "Unique identifier for connector profile resources",
      "type" : "string",
      "pattern" : "arn:aws:appflow:.*:[0-9]+:.*",
      "maxLength" : 512
    },
    "ConnectorLabel" : {
      "description" : "The label of the connector. The label is unique for each ConnectorRegistration in your AWS account. Only needed if calling for CUSTOMCONNECTOR connector type/.",
      "type" : "string",
      "pattern" : "[\\w!@#.-]+",
      "maxLength" : 256
    },
    "ConnectorProfileName" : {
      "description" : "The maximum number of items to retrieve in a single batch.",
      "type" : "string",
      "pattern" : "[\\w/!@#+=.-]+",
      "maxLength" : 256
    },
    "KMSArn" : {
      "description" : "The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.",
      "type" : "string",
      "pattern" : "arn:aws:kms:.*:[0-9]+:.*",
      "maxLength" : 2048,
      "minLength" : 20
    },
    "ConnectorType" : {
      "description" : "List of Saas providers that need connector profile to be created",
      "$ref" : "#/definitions/ConnectorType"
    },
    "ConnectionMode" : {
      "description" : "Mode in which data transfer should be enabled. Private connection mode is currently enabled for Salesforce, Snowflake, Trendmicro and Singular",
      "type" : "string",
      "enum" : [ "Public", "Private" ]
    },
    "ConnectorProfileConfig" : {
      "description" : "Connector specific configurations needed to create connector profile",
      "$ref" : "#/definitions/ConnectorProfileConfig"
    },
    "CredentialsArn" : {
      "description" : "A unique Arn for Connector-Profile resource",
      "type" : "string",
      "pattern" : "arn:aws:.*:.*:[0-9]+:.*",
      "maxLength" : 512
    }
  },
  "definitions" : {
    "ConnectorType" : {
      "type" : "string",
      "enum" : [ "Salesforce", "Pardot", "Singular", "Slack", "Redshift", "Marketo", "Googleanalytics", "Zendesk", "Servicenow", "SAPOData", "Datadog", "Trendmicro", "Snowflake", "Dynatrace", "Infornexus", "Amplitude", "Veeva", "CustomConnector" ]
    },
    "ConnectorProfileConfig" : {
      "description" : "Connector specific configurations needed to create connector profile",
      "type" : "object",
      "properties" : {
        "ConnectorProfileProperties" : {
          "$ref" : "#/definitions/ConnectorProfileProperties"
        },
        "ConnectorProfileCredentials" : {
          "$ref" : "#/definitions/ConnectorProfileCredentials"
        }
      }
    },
    "ConnectorProfileProperties" : {
      "description" : "Connector specific properties needed to create connector profile - currently not needed for Amplitude, Trendmicro, Googleanalytics and Singular",
      "type" : "object",
      "properties" : {
        "Datadog" : {
          "$ref" : "#/definitions/DatadogConnectorProfileProperties"
        },
        "Dynatrace" : {
          "$ref" : "#/definitions/DynatraceConnectorProfileProperties"
        },
        "InforNexus" : {
          "$ref" : "#/definitions/InforNexusConnectorProfileProperties"
        },
        "Marketo" : {
          "$ref" : "#/definitions/MarketoConnectorProfileProperties"
        },
        "Redshift" : {
          "$ref" : "#/definitions/RedshiftConnectorProfileProperties"
        },
        "SAPOData" : {
          "$ref" : "#/definitions/SAPODataConnectorProfileProperties"
        },
        "Salesforce" : {
          "$ref" : "#/definitions/SalesforceConnectorProfileProperties"
        },
        "Pardot" : {
          "$ref" : "#/definitions/PardotConnectorProfileProperties"
        },
        "ServiceNow" : {
          "$ref" : "#/definitions/ServiceNowConnectorProfileProperties"
        },
        "Slack" : {
          "$ref" : "#/definitions/SlackConnectorProfileProperties"
        },
        "Snowflake" : {
          "$ref" : "#/definitions/SnowflakeConnectorProfileProperties"
        },
        "Veeva" : {
          "$ref" : "#/definitions/VeevaConnectorProfileProperties"
        },
        "Zendesk" : {
          "$ref" : "#/definitions/ZendeskConnectorProfileProperties"
        },
        "CustomConnector" : {
          "$ref" : "#/definitions/CustomConnectorProfileProperties"
        }
      }
    },
    "ConnectorProfileCredentials" : {
      "description" : "Connector specific configuration needed to create connector profile based on Authentication mechanism",
      "type" : "object",
      "properties" : {
        "Amplitude" : {
          "$ref" : "#/definitions/AmplitudeConnectorProfileCredentials"
        },
        "Datadog" : {
          "$ref" : "#/definitions/DatadogConnectorProfileCredentials"
        },
        "Dynatrace" : {
          "$ref" : "#/definitions/DynatraceConnectorProfileCredentials"
        },
        "GoogleAnalytics" : {
          "$ref" : "#/definitions/GoogleAnalyticsConnectorProfileCredentials"
        },
        "InforNexus" : {
          "$ref" : "#/definitions/InforNexusConnectorProfileCredentials"
        },
        "Marketo" : {
          "$ref" : "#/definitions/MarketoConnectorProfileCredentials"
        },
        "Redshift" : {
          "$ref" : "#/definitions/RedshiftConnectorProfileCredentials"
        },
        "SAPOData" : {
          "$ref" : "#/definitions/SAPODataConnectorProfileCredentials"
        },
        "Salesforce" : {
          "$ref" : "#/definitions/SalesforceConnectorProfileCredentials"
        },
        "Pardot" : {
          "$ref" : "#/definitions/PardotConnectorProfileCredentials"
        },
        "ServiceNow" : {
          "$ref" : "#/definitions/ServiceNowConnectorProfileCredentials"
        },
        "Singular" : {
          "$ref" : "#/definitions/SingularConnectorProfileCredentials"
        },
        "Slack" : {
          "$ref" : "#/definitions/SlackConnectorProfileCredentials"
        },
        "Snowflake" : {
          "$ref" : "#/definitions/SnowflakeConnectorProfileCredentials"
        },
        "Trendmicro" : {
          "$ref" : "#/definitions/TrendmicroConnectorProfileCredentials"
        },
        "Veeva" : {
          "$ref" : "#/definitions/VeevaConnectorProfileCredentials"
        },
        "Zendesk" : {
          "$ref" : "#/definitions/ZendeskConnectorProfileCredentials"
        },
        "CustomConnector" : {
          "$ref" : "#/definitions/CustomConnectorProfileCredentials"
        }
      }
    },
    "AmplitudeConnectorProfileCredentials" : {
      "type" : "object",
      "required" : [ "ApiKey", "SecretKey" ],
      "properties" : {
        "ApiKey" : {
          "description" : "A unique alphanumeric identiﬁer used to authenticate a user, developer, or calling program to your API.",
          "$ref" : "#/definitions/ApiKey"
        },
        "SecretKey" : {
          "$ref" : "#/definitions/SecretKey"
        }
      }
    },
    "DatadogConnectorProfileCredentials" : {
      "type" : "object",
      "required" : [ "ApiKey", "ApplicationKey" ],
      "properties" : {
        "ApiKey" : {
          "description" : "A unique alphanumeric identiﬁer used to authenticate a user, developer, or calling program to your API.",
          "$ref" : "#/definitions/ApiKey"
        },
        "ApplicationKey" : {
          "description" : "Application keys, in conjunction with your API key, give you full access to Datadog’s programmatic API. Application keys are associated with the user account that created them. The application key is used to log all requests made to the API.",
          "$ref" : "#/definitions/ApplicationKey"
        }
      }
    },
    "DatadogConnectorProfileProperties" : {
      "type" : "object",
      "required" : [ "InstanceUrl" ],
      "properties" : {
        "InstanceUrl" : {
          "description" : "The location of the Datadog resource",
          "$ref" : "#/definitions/InstanceUrl"
        }
      }
    },
    "DynatraceConnectorProfileCredentials" : {
      "type" : "object",
      "required" : [ "ApiToken" ],
      "properties" : {
        "ApiToken" : {
          "description" : "The API tokens used by Dynatrace API to authenticate various API calls.",
          "$ref" : "#/definitions/ApiToken"
        }
      }
    },
    "DynatraceConnectorProfileProperties" : {
      "type" : "object",
      "required" : [ "InstanceUrl" ],
      "properties" : {
        "InstanceUrl" : {
          "description" : "The location of the Dynatrace resource",
          "$ref" : "#/definitions/InstanceUrl"
        }
      }
    },
    "GoogleAnalyticsConnectorProfileCredentials" : {
      "type" : "object",
      "required" : [ "ClientId", "ClientSecret" ],
      "properties" : {
        "ClientId" : {
          "description" : "The identiﬁer for the desired client.",
          "$ref" : "#/definitions/ClientId"
        },
        "ClientSecret" : {
          "description" : "The client secret used by the oauth client to authenticate to the authorization server.",
          "$ref" : "#/definitions/ClientSecret"
        },
        "AccessToken" : {
          "description" : "The credentials used to access protected resources.",
          "$ref" : "#/definitions/AccessToken"
        },
        "RefreshToken" : {
          "description" : "The credentials used to acquire new access tokens.",
          "$ref" : "#/definitions/RefreshToken"
        },
        "ConnectorOAuthRequest" : {
          "description" : "The oauth needed to request security tokens from the connector endpoint.",
          "$ref" : "#/definitions/ConnectorOAuthRequest"
        }
      }
    },
    "InforNexusConnectorProfileCredentials" : {
      "type" : "object",
      "required" : [ "AccessKeyId", "UserId", "SecretAccessKey", "Datakey" ],
      "properties" : {
        "AccessKeyId" : {
          "description" : "The Access Key portion of the credentials.",
          "$ref" : "#/definitions/AccessKeyId"
        },
        "UserId" : {
          "description" : "The identiﬁer for the user.",
          "$ref" : "#/definitions/Username"
        },
        "SecretAccessKey" : {
          "description" : "The secret key used to sign requests.",
          "$ref" : "#/definitions/Key"
        },
        "Datakey" : {
          "description" : "The encryption keys used to encrypt data.",
          "$ref" : "#/definitions/Key"
        }
      }
    },
    "InforNexusConnectorProfileProperties" : {
      "type" : "object",
      "required" : [ "InstanceUrl" ],
      "properties" : {
        "InstanceUrl" : {
          "description" : "The location of the InforNexus resource",
          "$ref" : "#/definitions/InstanceUrl"
        }
      }
    },
    "MarketoConnectorProfileCredentials" : {
      "type" : "object",
      "required" : [ "ClientId", "ClientSecret" ],
      "properties" : {
        "ClientId" : {
          "description" : "The identiﬁer for the desired client.",
          "$ref" : "#/definitions/ClientId"
        },
        "ClientSecret" : {
          "description" : "The client secret used by the oauth client to authenticate to the authorization server.",
          "$ref" : "#/definitions/ClientSecret"
        },
        "AccessToken" : {
          "description" : "The credentials used to access protected resources.",
          "$ref" : "#/definitions/AccessToken"
        },
        "ConnectorOAuthRequest" : {
          "description" : "The oauth needed to request security tokens from the connector endpoint.",
          "$ref" : "#/definitions/ConnectorOAuthRequest"
        }
      }
    },
    "MarketoConnectorProfileProperties" : {
      "type" : "object",
      "required" : [ "InstanceUrl" ],
      "properties" : {
        "InstanceUrl" : {
          "description" : "The location of the Marketo resource",
          "$ref" : "#/definitions/InstanceUrl"
        }
      }
    },
    "RedshiftConnectorProfileCredentials" : {
      "type" : "object",
      "properties" : {
        "Username" : {
          "description" : "The name of the user.",
          "$ref" : "#/definitions/Username"
        },
        "Password" : {
          "description" : "The password that corresponds to the username.",
          "$ref" : "#/definitions/Password"
        }
      }
    },
    "RedshiftConnectorProfileProperties" : {
      "type" : "object",
      "required" : [ "BucketName", "RoleArn" ],
      "properties" : {
        "DatabaseUrl" : {
          "description" : "The JDBC URL of the Amazon Redshift cluster.",
          "$ref" : "#/definitions/DatabaseUrl"
        },
        "BucketName" : {
          "description" : "The name of the Amazon S3 bucket associated with Redshift.",
          "$ref" : "#/definitions/BucketName"
        },
        "BucketPrefix" : {
          "description" : "The object key for the destination bucket in which Amazon AppFlow will place the ﬁles.",
          "$ref" : "#/definitions/BucketPrefix"
        },
        "RoleArn" : {
          "description" : "The Amazon Resource Name (ARN) of the IAM role.",
          "$ref" : "#/definitions/RoleArn"
        },
        "IsRedshiftServerless" : {
          "description" : "If Amazon AppFlow will connect to Amazon Redshift Serverless or Amazon Redshift cluster.",
          "type" : "boolean"
        },
        "DataApiRoleArn" : {
          "description" : "The Amazon Resource Name (ARN) of the IAM role that grants Amazon AppFlow access to the data through the Amazon Redshift Data API.",
          "$ref" : "#/definitions/DataApiRoleArn"
        },
        "ClusterIdentifier" : {
          "description" : "The unique identifier of the Amazon Redshift cluster.",
          "$ref" : "#/definitions/ClusterIdentifier"
        },
        "WorkgroupName" : {
          "description" : "The name of the Amazon Redshift serverless workgroup",
          "$ref" : "#/definitions/WorkgroupName"
        },
        "DatabaseName" : {
          "description" : "The name of the Amazon Redshift database that will store the transferred data.",
          "$ref" : "#/definitions/DatabaseName"
        }
      }
    },
    "SAPODataConnectorProfileCredentials" : {
      "type" : "object",
      "properties" : {
        "BasicAuthCredentials" : {
          "$ref" : "#/definitions/BasicAuthCredentials"
        },
        "OAuthCredentials" : {
          "type" : "object",
          "properties" : {
            "AccessToken" : {
              "$ref" : "#/definitions/AccessToken"
            },
            "RefreshToken" : {
              "$ref" : "#/definitions/RefreshToken"
            },
            "ConnectorOAuthRequest" : {
              "$ref" : "#/definitions/ConnectorOAuthRequest"
            },
            "ClientId" : {
              "$ref" : "#/definitions/ClientId"
            },
            "ClientSecret" : {
              "$ref" : "#/definitions/ClientSecret"
            }
          }
        }
      }
    },
    "SAPODataConnectorProfileProperties" : {
      "type" : "object",
      "properties" : {
        "ApplicationHostUrl" : {
          "$ref" : "#/definitions/ApplicationHostUrl"
        },
        "ApplicationServicePath" : {
          "$ref" : "#/definitions/ApplicationServicePath"
        },
        "PortNumber" : {
          "$ref" : "#/definitions/PortNumber"
        },
        "ClientNumber" : {
          "$ref" : "#/definitions/ClientNumber"
        },
        "LogonLanguage" : {
          "$ref" : "#/definitions/LogonLanguage"
        },
        "PrivateLinkServiceName" : {
          "$ref" : "#/definitions/PrivateLinkServiceName"
        },
        "OAuthProperties" : {
          "$ref" : "#/definitions/OAuthProperties"
        },
        "DisableSSO" : {
          "description" : "If you set this parameter to True, Amazon AppFlow bypasses the single sign-on (SSO) settings in your SAP account when it accesses your SAP OData instance.",
          "type" : "boolean"
        }
      }
    },
    "SalesforceConnectorProfileCredentials" : {
      "type" : "object",
      "properties" : {
        "AccessToken" : {
          "description" : "The credentials used to access protected resources.",
          "$ref" : "#/definitions/AccessToken"
        },
        "RefreshToken" : {
          "description" : "The credentials used to acquire new access tokens.",
          "$ref" : "#/definitions/RefreshToken"
        },
        "ConnectorOAuthRequest" : {
          "description" : "The oauth needed to request security tokens from the connector endpoint.",
          "$ref" : "#/definitions/ConnectorOAuthRequest"
        },
        "ClientCredentialsArn" : {
          "description" : "The client credentials to fetch access token and refresh token.",
          "$ref" : "#/definitions/ClientCredentialsArn"
        },
        "OAuth2GrantType" : {
          "description" : "The grant types to fetch an access token",
          "$ref" : "#/definitions/OAuth2GrantType"
        },
        "JwtToken" : {
          "description" : "The credentials used to access your Salesforce records",
          "$ref" : "#/definitions/JwtToken"
        }
      }
    },
    "SalesforceConnectorProfileProperties" : {
      "type" : "object",
      "properties" : {
        "InstanceUrl" : {
          "description" : "The location of the Salesforce resource",
          "$ref" : "#/definitions/InstanceUrl"
        },
        "isSandboxEnvironment" : {
          "description" : "Indicates whether the connector profile applies to a sandbox or production environment",
          "type" : "boolean"
        },
        "usePrivateLinkForMetadataAndAuthorization" : {
          "description" : "Indicates whether to make Metadata And Authorization calls over Pivate Network",
          "type" : "boolean"
        }
      }
    },
    "PardotConnectorProfileProperties" : {
      "type" : "object",
      "required" : [ "BusinessUnitId" ],
      "properties" : {
        "InstanceUrl" : {
          "description" : "The location of the Salesforce Pardot resource",
          "$ref" : "#/definitions/InstanceUrl"
        },
        "IsSandboxEnvironment" : {
          "description" : "Indicates whether the connector profile applies to a demo or production environment",
          "type" : "boolean"
        },
        "BusinessUnitId" : {
          "description" : "The Business unit id of Salesforce Pardot instance to be connected",
          "$ref" : "#/definitions/BusinessUnitId"
        }
      }
    },
    "PardotConnectorProfileCredentials" : {
      "type" : "object",
      "properties" : {
        "AccessToken" : {
          "description" : "The credentials used to access protected resources.",
          "$ref" : "#/definitions/AccessToken"
        },
        "RefreshToken" : {
          "description" : "The credentials used to acquire new access tokens.",
          "$ref" : "#/definitions/RefreshToken"
        },
        "ConnectorOAuthRequest" : {
          "description" : "The oauth needed to request security tokens from the connector endpoint.",
          "$ref" : "#/definitions/ConnectorOAuthRequest"
        },
        "ClientCredentialsArn" : {
          "description" : "The client credentials to fetch access token and refresh token.",
          "$ref" : "#/definitions/ClientCredentialsArn"
        }
      }
    },
    "ServiceNowConnectorProfileCredentials" : {
      "type" : "object",
      "properties" : {
        "Username" : {
          "description" : "The name of the user.",
          "$ref" : "#/definitions/Username"
        },
        "Password" : {
          "description" : "The password that corresponds to the username.",
          "$ref" : "#/definitions/Password"
        },
        "OAuth2Credentials" : {
          "description" : "The OAuth 2.0 credentials required to authenticate the user.",
          "$ref" : "#/definitions/OAuth2Credentials"
        }
      }
    },
    "ServiceNowConnectorProfileProperties" : {
      "type" : "object",
      "required" : [ "InstanceUrl" ],
      "properties" : {
        "InstanceUrl" : {
          "description" : "The location of the ServiceNow resource",
          "$ref" : "#/definitions/InstanceUrl"
        }
      }
    },
    "SingularConnectorProfileCredentials" : {
      "type" : "object",
      "required" : [ "ApiKey" ],
      "properties" : {
        "ApiKey" : {
          "description" : "A unique alphanumeric identiﬁer used to authenticate a user, developer, or calling program to your API.",
          "$ref" : "#/definitions/ApiKey"
        }
      }
    },
    "SlackConnectorProfileCredentials" : {
      "type" : "object",
      "required" : [ "ClientId", "ClientSecret" ],
      "properties" : {
        "ClientId" : {
          "description" : "The identiﬁer for the desired client.",
          "$ref" : "#/definitions/ClientId"
        },
        "ClientSecret" : {
          "description" : "The client secret used by the oauth client to authenticate to the authorization server.",
          "$ref" : "#/definitions/ClientSecret"
        },
        "AccessToken" : {
          "description" : "The credentials used to access protected resources.",
          "$ref" : "#/definitions/AccessToken"
        },
        "ConnectorOAuthRequest" : {
          "description" : "The oauth needed to request security tokens from the connector endpoint.",
          "$ref" : "#/definitions/ConnectorOAuthRequest"
        }
      }
    },
    "SlackConnectorProfileProperties" : {
      "type" : "object",
      "required" : [ "InstanceUrl" ],
      "properties" : {
        "InstanceUrl" : {
          "description" : "The location of the Slack resource",
          "$ref" : "#/definitions/InstanceUrl"
        }
      }
    },
    "SnowflakeConnectorProfileCredentials" : {
      "type" : "object",
      "required" : [ "Username", "Password" ],
      "properties" : {
        "Username" : {
          "description" : "The name of the user.",
          "$ref" : "#/definitions/Username"
        },
        "Password" : {
          "description" : "The password that corresponds to the username.",
          "$ref" : "#/definitions/Password"
        }
      }
    },
    "SnowflakeConnectorProfileProperties" : {
      "type" : "object",
      "required" : [ "Warehouse", "Stage", "BucketName" ],
      "properties" : {
        "Warehouse" : {
          "description" : "The name of the Snowﬂake warehouse.",
          "$ref" : "#/definitions/Warehouse"
        },
        "Stage" : {
          "description" : "The name of the Amazon S3 stage that was created while setting up an Amazon S3 stage in the\nSnowﬂake account. This is written in the following format: < Database>< Schema><Stage Name>.",
          "$ref" : "#/definitions/Stage"
        },
        "BucketName" : {
          "description" : "The name of the Amazon S3 bucket associated with Snowﬂake.",
          "$ref" : "#/definitions/BucketName"
        },
        "BucketPrefix" : {
          "description" : "The bucket prefix that refers to the Amazon S3 bucket associated with Snowﬂake.",
          "$ref" : "#/definitions/BucketPrefix"
        },
        "PrivateLinkServiceName" : {
          "description" : "The Snowﬂake Private Link service name to be used for private data transfers.",
          "$ref" : "#/definitions/PrivateLinkServiceName"
        },
        "AccountName" : {
          "description" : "The name of the account.",
          "$ref" : "#/definitions/AccountName"
        },
        "Region" : {
          "description" : "The region of the Snowﬂake account.",
          "$ref" : "#/definitions/Region"
        }
      }
    },
    "TrendmicroConnectorProfileCredentials" : {
      "type" : "object",
      "required" : [ "ApiSecretKey" ],
      "properties" : {
        "ApiSecretKey" : {
          "description" : "The Secret Access Key portion of the credentials.",
          "$ref" : "#/definitions/ApiSecretKey"
        }
      }
    },
    "VeevaConnectorProfileCredentials" : {
      "type" : "object",
      "required" : [ "Username", "Password" ],
      "properties" : {
        "Username" : {
          "description" : "The name of the user.",
          "$ref" : "#/definitions/Username"
        },
        "Password" : {
          "description" : "The password that corresponds to the username.",
          "$ref" : "#/definitions/Password"
        }
      }
    },
    "VeevaConnectorProfileProperties" : {
      "type" : "object",
      "required" : [ "InstanceUrl" ],
      "properties" : {
        "InstanceUrl" : {
          "description" : "The location of the Veeva resource",
          "$ref" : "#/definitions/InstanceUrl"
        }
      }
    },
    "ZendeskConnectorProfileCredentials" : {
      "type" : "object",
      "required" : [ "ClientId", "ClientSecret" ],
      "properties" : {
        "ClientId" : {
          "description" : "The identiﬁer for the desired client.",
          "$ref" : "#/definitions/ClientId"
        },
        "ClientSecret" : {
          "description" : "The client secret used by the oauth client to authenticate to the authorization server.",
          "$ref" : "#/definitions/ClientSecret"
        },
        "AccessToken" : {
          "description" : "The credentials used to access protected resources.",
          "$ref" : "#/definitions/AccessToken"
        },
        "ConnectorOAuthRequest" : {
          "description" : "The oauth needed to request security tokens from the connector endpoint.",
          "$ref" : "#/definitions/ConnectorOAuthRequest"
        }
      }
    },
    "ZendeskConnectorProfileProperties" : {
      "type" : "object",
      "required" : [ "InstanceUrl" ],
      "properties" : {
        "InstanceUrl" : {
          "description" : "The location of the Zendesk resource",
          "$ref" : "#/definitions/InstanceUrl"
        }
      }
    },
    "CustomConnectorProfileCredentials" : {
      "type" : "object",
      "required" : [ "AuthenticationType" ],
      "properties" : {
        "AuthenticationType" : {
          "$ref" : "#/definitions/AuthenticationType"
        },
        "Basic" : {
          "$ref" : "#/definitions/BasicAuthCredentials"
        },
        "Oauth2" : {
          "$ref" : "#/definitions/OAuth2Credentials"
        },
        "ApiKey" : {
          "$ref" : "#/definitions/ApiKeyCredentials"
        },
        "Custom" : {
          "$ref" : "#/definitions/CustomAuthCredentials"
        }
      },
      "additionalProperties" : False
    },
    "CustomConnectorProfileProperties" : {
      "type" : "object",
      "properties" : {
        "ProfileProperties" : {
          "$ref" : "#/definitions/ProfileProperties"
        },
        "OAuth2Properties" : {
          "$ref" : "#/definitions/OAuth2Properties"
        }
      },
      "additionalProperties" : False
    },
    "ApiKeyCredentials" : {
      "type" : "object",
      "required" : [ "ApiKey" ],
      "properties" : {
        "ApiKey" : {
          "$ref" : "#/definitions/ApiKey"
        },
        "ApiSecretKey" : {
          "$ref" : "#/definitions/ApiSecretKey"
        }
      },
      "additionalProperties" : False
    },
    "CustomAuthCredentials" : {
      "type" : "object",
      "required" : [ "CustomAuthenticationType" ],
      "properties" : {
        "CustomAuthenticationType" : {
          "$ref" : "#/definitions/CustomAuthenticationType"
        },
        "CredentialsMap" : {
          "$ref" : "#/definitions/CredentialsMap"
        }
      },
      "additionalProperties" : False
    },
    "CredentialsMap" : {
      "description" : "A map for properties for custom authentication.",
      "type" : "object",
      "patternProperties" : {
        "^[\\w]{1,128}$" : {
          "description" : "A string containing the value for the property",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 2048,
          "pattern" : "\\S+"
        }
      },
      "required" : [ ],
      "additionalProperties" : False
    },
    "OAuth2Credentials" : {
      "type" : "object",
      "properties" : {
        "ClientId" : {
          "$ref" : "#/definitions/ClientId"
        },
        "ClientSecret" : {
          "$ref" : "#/definitions/ClientSecret"
        },
        "AccessToken" : {
          "$ref" : "#/definitions/AccessToken"
        },
        "RefreshToken" : {
          "$ref" : "#/definitions/RefreshToken"
        },
        "OAuthRequest" : {
          "$ref" : "#/definitions/ConnectorOAuthRequest"
        }
      },
      "additionalProperties" : False
    },
    "BasicAuthCredentials" : {
      "type" : "object",
      "required" : [ "Username", "Password" ],
      "properties" : {
        "Username" : {
          "$ref" : "#/definitions/Username"
        },
        "Password" : {
          "$ref" : "#/definitions/Password"
        }
      },
      "additionalProperties" : False
    },
    "AuthenticationType" : {
      "type" : "string",
      "enum" : [ "OAUTH2", "APIKEY", "BASIC", "CUSTOM" ]
    },
    "OAuth2Properties" : {
      "type" : "object",
      "properties" : {
        "TokenUrl" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256,
          "pattern" : "^(https?)://[-a-zA-Z0-9+&amp;@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&amp;@#/%=~_|]"
        },
        "OAuth2GrantType" : {
          "$ref" : "#/definitions/OAuth2GrantType"
        },
        "TokenUrlCustomProperties" : {
          "$ref" : "#/definitions/TokenUrlCustomProperties"
        }
      },
      "additionalProperties" : False
    },
    "ProfileProperties" : {
      "description" : "A map for properties for custom connector.",
      "type" : "object",
      "patternProperties" : {
        "^[\\w]{1,256}$" : {
          "description" : "A string containing the value for the property",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 2048,
          "pattern" : "\\S+"
        }
      },
      "required" : [ ],
      "additionalProperties" : False
    },
    "OAuth2GrantType" : {
      "type" : "string",
      "enum" : [ "CLIENT_CREDENTIALS", "AUTHORIZATION_CODE", "JWT_BEARER" ]
    },
    "TokenUrlCustomProperties" : {
      "description" : "A map for properties for custom connector Token Url.",
      "type" : "object",
      "patternProperties" : {
        "^[\\w]{1,128}$" : {
          "description" : "A string containing the value for the property",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 2048,
          "pattern" : "\\S+"
        }
      },
      "required" : [ ],
      "additionalProperties" : False
    },
    "CustomAuthenticationType" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 256
    },
    "ClientId" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 512
    },
    "ClientSecret" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 512
    },
    "InstanceUrl" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 256
    },
    "AccessToken" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 4096
    },
    "ApiKey" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 256
    },
    "ApiSecretKey" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 256
    },
    "ApiToken" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 256
    },
    "ApplicationKey" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 512
    },
    "AuthCode" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 4096
    },
    "BucketName" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 63,
      "minLength" : 3
    },
    "BucketPrefix" : {
      "type" : "string",
      "maxLength" : 128
    },
    "Key" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 512
    },
    "DatabaseUrl" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 512
    },
    "RoleArn" : {
      "type" : "string",
      "pattern" : "arn:aws:iam:.*:[0-9]+:.*",
      "maxLength" : 512
    },
    "DataApiRoleArn" : {
      "type" : "string",
      "pattern" : "arn:aws:iam:.*:[0-9]+:.*",
      "maxLength" : 512
    },
    "ClusterIdentifier" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 512
    },
    "WorkgroupName" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 512
    },
    "DatabaseName" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 512
    },
    "Warehouse" : {
      "type" : "string",
      "pattern" : "[\\s\\w/!@#+=.-]*",
      "maxLength" : 512
    },
    "Stage" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 512
    },
    "PrivateLinkServiceName" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 512
    },
    "AccountName" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 512
    },
    "JwtToken" : {
      "type" : "string",
      "pattern" : "^[A-Za-z0-9-_=]+\\.[A-Za-z0-9-_=]+\\.[A-Za-z0-9-_.+/=]*$",
      "maxLength" : 8000
    },
    "RefreshToken" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 4096
    },
    "Region" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 64
    },
    "SecretKey" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 256
    },
    "AccessKeyId" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 256
    },
    "Username" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 512
    },
    "Password" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 512
    },
    "BusinessUnitId" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 18
    },
    "ConnectorOAuthRequest" : {
      "type" : "object",
      "properties" : {
        "AuthCode" : {
          "description" : "The code provided by the connector when it has been authenticated via the connected app.",
          "type" : "string"
        },
        "RedirectUri" : {
          "description" : "The URL to which the authentication server redirects the browser after authorization has been\ngranted.",
          "type" : "string"
        }
      }
    },
    "ClientCredentialsArn" : {
      "type" : "string",
      "pattern" : "arn:aws:secretsmanager:.*:[0-9]+:.*",
      "maxLength" : 2048
    },
    "ApplicationHostUrl" : {
      "type" : "string",
      "maxLength" : 256,
      "pattern" : "^(https?)://[-a-zA-Z0-9+&amp;@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&amp;@#/%=~_|]"
    },
    "ApplicationServicePath" : {
      "type" : "string",
      "pattern" : "\\S+",
      "maxLength" : 512
    },
    "ClientNumber" : {
      "type" : "string",
      "pattern" : "^\\d{3}$",
      "minLength" : 3,
      "maxLength" : 3
    },
    "LogonLanguage" : {
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_]*$",
      "maxLength" : 2
    },
    "PortNumber" : {
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 65535
    },
    "OAuthProperties" : {
      "type" : "object",
      "properties" : {
        "AuthCodeUrl" : {
          "type" : "string",
          "maxLength" : 256,
          "pattern" : "^(https?)://[-a-zA-Z0-9+&amp;@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&amp;@#/%=~_|]"
        },
        "TokenUrl" : {
          "type" : "string",
          "maxLength" : 256,
          "pattern" : "^(https?)://[-a-zA-Z0-9+&amp;@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&amp;@#/%=~_|]"
        },
        "OAuthScopes" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "type" : "string",
            "maxLength" : 128,
            "pattern" : "[/\\w]*"
          }
        }
      }
    }
  },
  "required" : [ "ConnectorProfileName", "ConnectionMode", "ConnectorType" ],
  "createOnlyProperties" : [ "/properties/ConnectorProfileName", "/properties/ConnectorType", "/properties/ConnectorLabel" ],
  "readOnlyProperties" : [ "/properties/ConnectorProfileArn", "/properties/CredentialsArn" ],
  "writeOnlyProperties" : [ "/properties/ConnectorProfileConfig", "/properties/KMSArn" ],
  "primaryIdentifier" : [ "/properties/ConnectorProfileName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "appflow:CreateConnectorProfile", "kms:ListKeys", "kms:DescribeKey", "kms:ListAliases", "kms:CreateGrant", "kms:ListGrants", "iam:PassRole", "secretsmanager:CreateSecret", "secretsmanager:GetSecretValue", "secretsmanager:PutResourcePolicy" ]
    },
    "delete" : {
      "permissions" : [ "appflow:DeleteConnectorProfile" ]
    },
    "list" : {
      "permissions" : [ "appflow:DescribeConnectorProfiles" ]
    },
    "read" : {
      "permissions" : [ "appflow:DescribeConnectorProfiles" ]
    },
    "update" : {
      "permissions" : [ "appflow:UpdateConnectorProfile", "kms:ListKeys", "kms:DescribeKey", "kms:ListAliases", "kms:CreateGrant", "kms:ListGrants", "iam:PassRole", "secretsmanager:CreateSecret", "secretsmanager:GetSecretValue", "secretsmanager:PutResourcePolicy" ]
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  }
}