SCHEMA = {
  "typeName" : "AWS::Transfer::WebApp",
  "description" : "Resource Type definition for AWS::Transfer::WebApp",
  "definitions" : {
    "IdentityProviderDetails" : {
      "type" : "object",
      "description" : "You can provide a structure that contains the details for the identity provider to use with your web app.",
      "properties" : {
        "ApplicationArn" : {
          "type" : "string",
          "maxLength" : 1224,
          "minLength" : 10,
          "pattern" : "^arn:[\\w-]+:sso::\\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}$"
        },
        "InstanceArn" : {
          "type" : "string",
          "description" : "The Amazon Resource Name (ARN) for the IAM Identity Center used for the web app.",
          "maxLength" : 1224,
          "minLength" : 10,
          "pattern" : "^arn:[\\w-]+:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$"
        },
        "Role" : {
          "type" : "string",
          "description" : "The IAM role in IAM Identity Center used for the web app.",
          "maxLength" : 2048,
          "minLength" : 20,
          "pattern" : "^arn:[a-z-]+:iam::[0-9]{12}:role[:/]\\S+$"
        }
      },
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "description" : "Key-value pair that can be used to group and search for web apps.",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 0
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "WebAppCustomization" : {
      "type" : "object",
      "properties" : {
        "Title" : {
          "description" : "Specifies a title to display on the web app.",
          "type" : "string",
          "maxLength" : 100,
          "minLength" : 0
        },
        "LogoFile" : {
          "description" : "Specifies a logo to display on the web app.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 51200
        },
        "FaviconFile" : {
          "description" : "Specifies a favicon to display in the browser tab.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 20960
        }
      },
      "additionalProperties" : False
    },
    "WebAppEndpointPolicy" : {
      "type" : "string",
      "enum" : [ "STANDARD", "FIPS" ]
    },
    "WebAppUnits" : {
      "oneOf" : [ {
        "type" : "object",
        "description" : "A union that contains the value for number of concurrent connections or the user sessions on your web app.",
        "title" : "Provisioned",
        "properties" : {
          "Provisioned" : {
            "type" : "integer",
            "minimum" : 1
          }
        },
        "required" : [ "Provisioned" ],
        "additionalProperties" : False
      } ]
    }
  },
  "properties" : {
    "Arn" : {
      "description" : "Specifies the unique Amazon Resource Name (ARN) for the web app.",
      "type" : "string",
      "pattern" : "arn:.*",
      "minLength" : 20,
      "maxLength" : 1600
    },
    "WebAppId" : {
      "description" : "A unique identifier for the web app.",
      "type" : "string",
      "pattern" : "^webapp-([0-9a-f]{17})$",
      "minLength" : 24,
      "maxLength" : 24
    },
    "IdentityProviderDetails" : {
      "$ref" : "#/definitions/IdentityProviderDetails"
    },
    "AccessEndpoint" : {
      "description" : "The AccessEndpoint is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1024
    },
    "WebAppUnits" : {
      "$ref" : "#/definitions/WebAppUnits"
    },
    "WebAppCustomization" : {
      "$ref" : "#/definitions/WebAppCustomization"
    },
    "WebAppEndpointPolicy" : {
      "$ref" : "#/definitions/WebAppEndpointPolicy"
    },
    "Tags" : {
      "type" : "array",
      "description" : "Key-value pairs that can be used to group and search for web apps.",
      "maxItems" : 50,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "IdentityProviderDetails" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/WebAppId", "/properties/IdentityProviderDetails/ApplicationArn" ],
  "createOnlyProperties" : [ "/properties/WebAppEndpointPolicy", "/properties/IdentityProviderDetails/InstanceArn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "additionalIdentifiers" : [ [ "/properties/WebAppId" ] ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "transfer:TagResource", "transfer:UnTagResource", "transfer:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "transfer:CreateWebApp", "transfer:DescribeWebApp", "transfer:DescribeWebAppCustomization", "transfer:TagResource", "transfer:UpdateWebAppCustomization", "iam:PassRole", "sso:CreateApplication", "sso:DescribeApplication", "sso:ListApplications", "sso:PutApplicationGrant", "sso:GetApplicationGrant", "sso:ListApplicationGrants", "sso:PutApplicationAuthenticationMethod", "sso:GetApplicationAuthenticationMethod", "sso:ListApplicationAuthenticationMethods", "sso:PutApplicationAccessScope", "sso:GetApplicationAccessScope", "sso:ListApplicationAccessScopes" ]
    },
    "read" : {
      "permissions" : [ "transfer:DescribeWebApp", "transfer:DescribeWebAppCustomization" ]
    },
    "update" : {
      "permissions" : [ "transfer:DescribeWebApp", "transfer:DescribeWebAppCustomization", "transfer:UpdateWebApp", "transfer:UpdateWebAppCustomization", "transfer:DeleteWebAppCustomization", "transfer:UnTagResource", "transfer:TagResource", "iam:PassRole", "sso:PutApplicationGrant", "sso:GetApplicationGrant", "sso:ListApplicationGrants", "sso:UpdateApplication", "sso:DescribeApplication", "sso:ListApplications" ]
    },
    "delete" : {
      "permissions" : [ "transfer:DeleteWebApp", "sso:DescribeApplication", "sso:DeleteApplication" ]
    },
    "list" : {
      "permissions" : [ "transfer:ListWebApps" ]
    }
  }
}