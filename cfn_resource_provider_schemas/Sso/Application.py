SCHEMA = {
  "typeName" : "AWS::SSO::Application",
  "description" : "Resource Type definition for Identity Center (SSO) Application",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-sso/aws-sso-application",
  "definitions" : {
    "Tag" : {
      "description" : "The metadata that you apply to the Identity Center (SSO) Application to help you categorize and organize them.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "pattern" : "^[\\w+=,.@-]+$",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "pattern" : "^[\\w+=,.@-]+$",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "SignInOptions" : {
      "description" : "A structure that describes the sign-in options for an application portal",
      "type" : "object",
      "properties" : {
        "Origin" : {
          "description" : "This determines how IAM Identity Center navigates the user to the target application",
          "type" : "string",
          "enum" : [ "IDENTITY_CENTER", "APPLICATION" ]
        },
        "ApplicationUrl" : {
          "description" : "The URL that accepts authentication requests for an application, this is a required parameter if the Origin parameter is APPLICATION",
          "type" : "string",
          "pattern" : "^http(s)?:\\/\\/[-a-zA-Z0-9+&@#\\/%?=~_|!:,.;]*[-a-zA-Z0-9+&bb@#\\/%?=~_|]$",
          "minLength" : 1,
          "maxLength" : 512
        }
      },
      "required" : [ "Origin" ],
      "additionalProperties" : False
    },
    "PortalOptionsConfiguration" : {
      "description" : "A structure that describes the options for the access portal associated with an application",
      "type" : "object",
      "properties" : {
        "Visibility" : {
          "description" : "Indicates whether this application is visible in the access portal",
          "type" : "string",
          "enum" : [ "ENABLED", "DISABLED" ]
        },
        "SignInOptions" : {
          "description" : "A structure that describes the sign-in options for the access portal",
          "$ref" : "#/definitions/SignInOptions"
        }
      },
      "required" : [ ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Name" : {
      "description" : "The name you want to assign to this Identity Center (SSO) Application",
      "type" : "string",
      "pattern" : "^[\\w+=,.@-]+$",
      "minLength" : 0,
      "maxLength" : 255
    },
    "Description" : {
      "description" : "The description information for the Identity Center (SSO) Application",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128
    },
    "InstanceArn" : {
      "description" : "The ARN of the instance of IAM Identity Center under which the operation will run",
      "type" : "string",
      "pattern" : "^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$",
      "minLength" : 10,
      "maxLength" : 1224
    },
    "ApplicationArn" : {
      "description" : "The Application ARN that is returned upon creation of the Identity Center (SSO) Application",
      "type" : "string",
      "pattern" : "^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}$",
      "minLength" : 10,
      "maxLength" : 1224
    },
    "ApplicationProviderArn" : {
      "description" : "The ARN of the application provider under which the operation will run",
      "type" : "string",
      "pattern" : "^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::aws:applicationProvider/[a-zA-Z0-9-/]+$",
      "minLength" : 10,
      "maxLength" : 1224
    },
    "Status" : {
      "description" : "Specifies whether the application is enabled or disabled",
      "type" : "string",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "PortalOptions" : {
      "description" : "A structure that describes the options for the portal associated with an application",
      "$ref" : "#/definitions/PortalOptionsConfiguration"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "description" : "Specifies tags to be attached to the application",
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 75
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name", "InstanceArn", "ApplicationProviderArn" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "sso:TagResource", "sso:UntagResource" ]
  },
  "createOnlyProperties" : [ "/properties/InstanceArn", "/properties/ApplicationProviderArn" ],
  "readOnlyProperties" : [ "/properties/ApplicationArn" ],
  "primaryIdentifier" : [ "/properties/ApplicationArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "sso:CreateApplication", "sso:DescribeApplication", "sso:TagResource", "sso:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "sso:DescribeApplication", "sso:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "sso:UpdateApplication", "sso:TagResource", "sso:UntagResource", "sso:ListTagsForResource", "sso:DescribeApplication" ]
    },
    "delete" : {
      "permissions" : [ "sso:DeleteApplication" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "InstanceArn" : {
            "$ref" : "resource-schema.json#/properties/InstanceArn"
          }
        },
        "required" : [ "InstanceArn" ]
      },
      "permissions" : [ "sso:ListApplications", "sso:ListTagsForResource" ]
    }
  }
}