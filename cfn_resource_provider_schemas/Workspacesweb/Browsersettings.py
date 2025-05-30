SCHEMA = {
  "typeName" : "AWS::WorkSpacesWeb::BrowserSettings",
  "description" : "Definition of AWS::WorkSpacesWeb::BrowserSettings Resource Type",
  "definitions" : {
    "EncryptionContextMap" : {
      "type" : "object",
      "patternProperties" : {
        "^[\\s\\S]*$" : {
          "type" : "string",
          "maxLength" : 131072,
          "minLength" : 0,
          "pattern" : "^[\\s\\S]*$"
        }
      },
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "AdditionalEncryptionContext" : {
      "$ref" : "#/definitions/EncryptionContextMap"
    },
    "AssociatedPortalArns" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "maxLength" : 2048,
        "minLength" : 20,
        "pattern" : "^arn:[\\w+=\\/,.@-]+:[a-zA-Z0-9\\-]+:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\\/[a-fA-F0-9\\-]{36})+$"
      },
      "insertionOrder" : False
    },
    "BrowserPolicy" : {
      "type" : "string",
      "maxLength" : 131072,
      "minLength" : 2,
      "pattern" : "\\{[\\S\\s]*\\}\\s*"
    },
    "BrowserSettingsArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:[\\w+=\\/,.@-]+:[a-zA-Z0-9\\-]+:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\\/[a-fA-F0-9\\-]{36})+$"
    },
    "CustomerManagedKey" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:[\\w+=\\/,.@-]+:kms:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:key\\/[a-zA-Z0-9-]+$"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 200,
      "minItems" : 0,
      "insertionOrder" : False
    }
  },
  "readOnlyProperties" : [ "/properties/AssociatedPortalArns", "/properties/BrowserSettingsArn" ],
  "createOnlyProperties" : [ "/properties/AdditionalEncryptionContext", "/properties/CustomerManagedKey" ],
  "primaryIdentifier" : [ "/properties/BrowserSettingsArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "workspaces-web:CreateBrowserSettings", "workspaces-web:GetBrowserSettings", "workspaces-web:ListTagsForResource", "workspaces-web:TagResource", "kms:DescribeKey", "kms:GenerateDataKey", "kms:Decrypt", "kms:GenerateDataKeyWithoutPlaintext", "kms:ReEncryptTo", "kms:ReEncryptFrom" ]
    },
    "read" : {
      "permissions" : [ "workspaces-web:GetBrowserSettings", "workspaces-web:ListBrowserSettings", "workspaces-web:ListTagsForResource", "kms:CreateGrant", "kms:DescribeKey", "kms:GenerateDataKey", "kms:Decrypt" ]
    },
    "update" : {
      "permissions" : [ "workspaces-web:UpdateBrowserSettings", "workspaces-web:TagResource", "workspaces-web:UntagResource", "workspaces-web:GetBrowserSettings", "workspaces-web:ListBrowserSettings", "workspaces-web:ListTagsForResource", "kms:CreateGrant", "kms:DescribeKey", "kms:GenerateDataKey", "kms:Decrypt" ]
    },
    "delete" : {
      "permissions" : [ "workspaces-web:GetBrowserSettings", "workspaces-web:DeleteBrowserSettings", "kms:CreateGrant", "kms:DescribeKey", "kms:GenerateDataKey", "kms:Decrypt" ]
    },
    "list" : {
      "permissions" : [ "workspaces-web:ListBrowserSettings", "kms:Decrypt", "kms:DescribeKey" ]
    }
  },
  "tagging" : {
    "cloudFormationSystemTags" : False,
    "tagOnCreate" : True,
    "tagProperty" : "/properties/Tags",
    "tagUpdatable" : True,
    "taggable" : True,
    "permissions" : [ "workspaces-web:UntagResource", "workspaces-web:ListTagsForResource", "workspaces-web:TagResource" ]
  },
  "additionalProperties" : False
}