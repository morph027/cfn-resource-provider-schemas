SCHEMA = {
  "typeName" : "AWS::Grafana::Workspace",
  "description" : "Definition of AWS::Grafana::Workspace Resource Type",
  "definitions" : {
    "AssertionAttributes" : {
      "type" : "object",
      "description" : "Maps Grafana friendly names to the IdPs SAML attributes.",
      "properties" : {
        "Name" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "description" : "Name of the attribute within the SAML assert to use as the users name in Grafana."
        },
        "Login" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "description" : "Name of the attribute within the SAML assert to use as the users login handle in Grafana."
        },
        "Email" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "description" : "Name of the attribute within the SAML assert to use as the users email in Grafana."
        },
        "Groups" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "description" : "Name of the attribute within the SAML assert to use as the users groups in Grafana."
        },
        "Role" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "description" : "Name of the attribute within the SAML assert to use as the users roles in Grafana."
        },
        "Org" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "description" : "Name of the attribute within the SAML assert to use as the users organizations in Grafana."
        }
      },
      "additionalProperties" : False
    },
    "IdpMetadata" : {
      "type" : "object",
      "description" : "IdP Metadata used to configure SAML authentication in Grafana.",
      "properties" : {
        "Url" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 1,
          "description" : "URL that vends the IdPs metadata."
        },
        "Xml" : {
          "type" : "string",
          "description" : "XML blob of the IdPs metadata."
        }
      },
      "additionalProperties" : False
    },
    "RoleValues" : {
      "type" : "object",
      "description" : "Maps SAML roles to the Grafana Editor and Admin roles.",
      "properties" : {
        "Editor" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "type" : "string",
            "maxLength" : 256,
            "minLength" : 1,
            "description" : "A single SAML role."
          },
          "description" : "List of SAML roles which will be mapped into the Grafana Editor role."
        },
        "Admin" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "type" : "string",
            "maxLength" : 256,
            "minLength" : 1,
            "description" : "A single SAML role."
          },
          "description" : "List of SAML roles which will be mapped into the Grafana Admin role."
        }
      },
      "additionalProperties" : False
    },
    "SamlConfiguration" : {
      "type" : "object",
      "description" : "SAML configuration data associated with an AMG workspace.",
      "properties" : {
        "IdpMetadata" : {
          "$ref" : "#/definitions/IdpMetadata"
        },
        "AssertionAttributes" : {
          "$ref" : "#/definitions/AssertionAttributes"
        },
        "RoleValues" : {
          "$ref" : "#/definitions/RoleValues"
        },
        "AllowedOrganizations" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "type" : "string",
            "maxLength" : 256,
            "minLength" : 1,
            "description" : "A single SAML organization."
          },
          "description" : "List of SAML organizations allowed to access Grafana."
        },
        "LoginValidityDuration" : {
          "type" : "number",
          "description" : "The maximum lifetime an authenticated user can be logged in (in minutes) before being required to re-authenticate."
        }
      },
      "required" : [ "IdpMetadata" ],
      "additionalProperties" : False
    },
    "NetworkAccessControl" : {
      "type" : "object",
      "description" : "The configuration settings for Network Access Control.",
      "properties" : {
        "PrefixListIds" : {
          "type" : "array",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "minItems" : 0,
          "maxItems" : 5,
          "items" : {
            "type" : "string",
            "minLength" : 1,
            "description" : "Prefix List Ids"
          },
          "description" : "The list of prefix list IDs. A prefix list is a list of CIDR ranges of IP addresses. The IP addresses specified are allowed to access your workspace. If the list is not included in the configuration then no IP addresses will be allowed to access the workspace."
        },
        "VpceIds" : {
          "type" : "array",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "minItems" : 0,
          "maxItems" : 5,
          "items" : {
            "type" : "string",
            "minLength" : 1,
            "description" : "VPCE Ids"
          },
          "description" : "The list of Amazon VPC endpoint IDs for the workspace. If a NetworkAccessConfiguration is specified then only VPC endpoints specified here will be allowed to access the workspace."
        }
      },
      "additionalProperties" : False
    },
    "VpcConfiguration" : {
      "type" : "object",
      "description" : "The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.",
      "properties" : {
        "SecurityGroupIds" : {
          "type" : "array",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "minItems" : 1,
          "maxItems" : 5,
          "items" : {
            "type" : "string",
            "minLength" : 1,
            "maxLength" : 255,
            "description" : "VPC Security Group Id"
          },
          "description" : "The list of Amazon EC2 security group IDs attached to the Amazon VPC for your Grafana workspace to connect."
        },
        "SubnetIds" : {
          "type" : "array",
          "insertionOrder" : False,
          "uniqueItems" : True,
          "minItems" : 2,
          "maxItems" : 6,
          "items" : {
            "type" : "string",
            "minLength" : 1,
            "maxLength" : 255,
            "description" : "VPC Subnet Id"
          },
          "description" : "The list of Amazon EC2 subnet IDs created in the Amazon VPC for your Grafana workspace to connect."
        }
      },
      "required" : [ "SecurityGroupIds", "SubnetIds" ],
      "additionalProperties" : False
    },
    "AccountAccessType" : {
      "type" : "string",
      "description" : "These enums represent valid account access types. Specifically these enums determine whether the workspace can access AWS resources in the AWS account only, or whether it can also access resources in other accounts in the same organization. If the value CURRENT_ACCOUNT is used, a workspace role ARN must be provided. If the value is ORGANIZATION, a list of organizational units must be provided.",
      "enum" : [ "CURRENT_ACCOUNT", "ORGANIZATION" ]
    },
    "AuthenticationProviderTypes" : {
      "type" : "string",
      "description" : "Valid workspace authentication providers.",
      "enum" : [ "AWS_SSO", "SAML" ]
    },
    "DataSourceType" : {
      "type" : "string",
      "description" : "These enums represent valid AWS data sources that can be queried via the Grafana workspace. These data sources are primarily used to help customers visualize which data sources have been added to a service managed workspace IAM role.",
      "enum" : [ "AMAZON_OPENSEARCH_SERVICE", "CLOUDWATCH", "PROMETHEUS", "XRAY", "TIMESTREAM", "SITEWISE", "ATHENA", "REDSHIFT" ]
    },
    "NotificationDestinationType" : {
      "type" : "string",
      "description" : "These enums represent valid AWS notification destinations that the Grafana workspace has permission to use. These notification destinations are primarily used to help customers visualize which destinations have been added to a service managed IAM role.",
      "enum" : [ "SNS" ]
    },
    "PermissionType" : {
      "type" : "string",
      "description" : "These enums represent valid permission types to use when creating or configuring a Grafana workspace. The SERVICE_MANAGED permission type means the Managed Grafana service will create a workspace IAM role on your behalf. The CUSTOMER_MANAGED permission type means that the customer is expected to provide an IAM role that the Grafana workspace can use to query data sources.",
      "enum" : [ "CUSTOMER_MANAGED", "SERVICE_MANAGED" ]
    },
    "WorkspaceStatus" : {
      "type" : "string",
      "description" : "These enums represent the status of a workspace.",
      "enum" : [ "ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING", "UPGRADING", "VERSION_UPDATING", "DELETION_FAILED", "CREATION_FAILED", "UPDATE_FAILED", "UPGRADE_FAILED", "LICENSE_REMOVAL_FAILED", "VERSION_UPDATE_FAILED" ]
    },
    "SamlConfigurationStatus" : {
      "type" : "string",
      "description" : "Valid SAML configuration statuses.",
      "enum" : [ "CONFIGURED", "NOT_CONFIGURED" ]
    }
  },
  "properties" : {
    "AuthenticationProviders" : {
      "type" : "array",
      "insertionOrder" : False,
      "minItems" : 1,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/AuthenticationProviderTypes"
      },
      "description" : "List of authentication providers to enable."
    },
    "SsoClientId" : {
      "type" : "string",
      "description" : "The client ID of the AWS SSO Managed Application."
    },
    "SamlConfiguration" : {
      "$ref" : "#/definitions/SamlConfiguration"
    },
    "NetworkAccessControl" : {
      "$ref" : "#/definitions/NetworkAccessControl"
    },
    "VpcConfiguration" : {
      "$ref" : "#/definitions/VpcConfiguration"
    },
    "SamlConfigurationStatus" : {
      "$ref" : "#/definitions/SamlConfigurationStatus"
    },
    "ClientToken" : {
      "type" : "string",
      "pattern" : "^[!-~]{1,64}$",
      "description" : "A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request."
    },
    "Status" : {
      "$ref" : "#/definitions/WorkspaceStatus"
    },
    "CreationTimestamp" : {
      "type" : "string",
      "description" : "Timestamp when the workspace was created.",
      "format" : "date-time"
    },
    "ModificationTimestamp" : {
      "type" : "string",
      "description" : "Timestamp when the workspace was last modified",
      "format" : "date-time"
    },
    "GrafanaVersion" : {
      "type" : "string",
      "maxLength" : 255,
      "minLength" : 1,
      "description" : "The version of Grafana to support in your workspace."
    },
    "Endpoint" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 1,
      "description" : "Endpoint for the Grafana workspace."
    },
    "AccountAccessType" : {
      "$ref" : "#/definitions/AccountAccessType"
    },
    "OrganizationRoleName" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 1,
      "description" : "The name of an IAM role that already exists to use with AWS Organizations to access AWS data sources and notification channels in other accounts in an organization."
    },
    "PermissionType" : {
      "$ref" : "#/definitions/PermissionType"
    },
    "StackSetName" : {
      "type" : "string",
      "description" : "The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace."
    },
    "DataSources" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/DataSourceType"
      },
      "description" : "List of data sources on the service managed IAM role."
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 0,
      "description" : "Description of a workspace."
    },
    "Id" : {
      "type" : "string",
      "pattern" : "^g-[0-9a-f]{10}$",
      "description" : "The id that uniquely identifies a Grafana workspace."
    },
    "Name" : {
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9-._~]{1,255}$",
      "description" : "The user friendly name of a workspace."
    },
    "NotificationDestinations" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/NotificationDestinationType"
      },
      "description" : "List of notification destinations on the customers service managed IAM role that the Grafana workspace can query."
    },
    "OrganizationalUnits" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "description" : "Id of an organizational unit."
      },
      "description" : "List of Organizational Units containing AWS accounts the Grafana workspace can pull data from."
    },
    "RoleArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 1,
      "description" : "IAM Role that will be used to grant the Grafana workspace access to a customers AWS resources."
    },
    "PluginAdminEnabled" : {
      "type" : "boolean",
      "description" : "Allow workspace admins to install plugins"
    }
  },
  "required" : [ "AuthenticationProviders", "PermissionType", "AccountAccessType" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/SsoClientId", "/properties/SamlConfigurationStatus", "/properties/Endpoint", "/properties/Status", "/properties/CreationTimestamp", "/properties/ModificationTimestamp" ],
  "writeOnlyProperties" : [ "/properties/ClientToken" ],
  "createOnlyProperties" : [ "/properties/ClientToken" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "handlers" : {
    "create" : {
      "permissions" : [ "grafana:CreateWorkspace", "grafana:DescribeWorkspace", "grafana:DescribeWorkspaceAuthentication", "grafana:DescribeWorkspaceConfiguration", "grafana:UpdateWorkspaceAuthentication", "sso:DescribeRegisteredRegions", "sso:CreateManagedApplicationInstance", "organizations:DescribeOrganization", "sso:GetSharedSsoConfiguration", "iam:PassRole", "ec2:GetManagedPrefixListEntries", "ec2:DescribeSecurityGroups", "ec2:DescribeSubnets", "ec2:DescribeVpcs", "iam:CreateServiceLinkedRole", "sso:ListApplicationInstances", "sso:GetApplicationInstance" ]
    },
    "read" : {
      "permissions" : [ "grafana:DescribeWorkspace", "grafana:DescribeWorkspaceAuthentication", "grafana:DescribeWorkspaceConfiguration" ]
    },
    "update" : {
      "permissions" : [ "grafana:DescribeWorkspace", "grafana:DescribeWorkspaceAuthentication", "grafana:DescribeWorkspaceConfiguration", "grafana:UpdateWorkspace", "grafana:UpdateWorkspaceAuthentication", "grafana:UpdateWorkspaceConfiguration", "sso:DescribeRegisteredRegions", "sso:CreateManagedApplicationInstance", "ec2:GetManagedPrefixListEntries", "iam:PassRole", "ec2:DescribeSecurityGroups", "ec2:DescribeSubnets", "ec2:DescribeVpcs", "iam:CreateServiceLinkedRole", "sso:ListApplicationInstances", "sso:GetApplicationInstance" ]
    },
    "delete" : {
      "permissions" : [ "grafana:DeleteWorkspace", "grafana:DescribeWorkspace", "grafana:DescribeWorkspaceAuthentication", "grafana:DescribeWorkspaceConfiguration", "sso:DeleteManagedApplicationInstance", "sso:DescribeRegisteredRegions" ]
    },
    "list" : {
      "permissions" : [ "grafana:ListWorkspaces", "grafana:DescribeWorkspaceAuthentication", "grafana:DescribeWorkspaceConfiguration" ]
    }
  }
}