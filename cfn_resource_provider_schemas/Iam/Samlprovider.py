SCHEMA = {
  "typeName" : "AWS::IAM::SAMLProvider",
  "description" : "Resource Type definition for AWS::IAM::SAMLProvider",
  "additionalProperties" : False,
  "properties" : {
    "Name" : {
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "[\\w._-]+",
      "type" : "string"
    },
    "SamlMetadataDocument" : {
      "minLength" : 1000,
      "maxLength" : 10000000,
      "type" : "string"
    },
    "Arn" : {
      "description" : "Amazon Resource Name (ARN) of the SAML provider",
      "minLength" : 1,
      "maxLength" : 1600,
      "type" : "string"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "AssertionEncryptionMode" : {
      "description" : "The encryption setting for the SAML provider",
      "type" : "string",
      "enum" : [ "Allowed", "Required" ]
    },
    "AddPrivateKey" : {
      "description" : "The private key from your external identity provider",
      "minLength" : 1,
      "maxLength" : 16384,
      "pattern" : "[\\u0009\\u000A\\u000D\\u0020-\\u00FF]+",
      "type" : "string"
    },
    "RemovePrivateKey" : {
      "description" : "The Key ID of the private key to remove",
      "minLength" : 22,
      "maxLength" : 64,
      "pattern" : "[A-Z0-9]+",
      "type" : "string"
    },
    "PrivateKeyList" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/SAMLPrivateKey"
      },
      "maxItems" : 2
    },
    "SamlProviderUUID" : {
      "description" : "The unique identifier assigned to the SAML provider",
      "minLength" : 22,
      "maxLength" : 64,
      "pattern" : "[A-Z0-9]+",
      "type" : "string"
    }
  },
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        },
        "Key" : {
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "Value", "Key" ]
    },
    "SAMLPrivateKey" : {
      "description" : "The private key metadata for the SAML provider",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "KeyId" : {
          "description" : "The unique identifier for the SAML private key.",
          "minLength" : 22,
          "maxLength" : 64,
          "pattern" : "[A-Z0-9]+",
          "type" : "string"
        },
        "Timestamp" : {
          "description" : "The date and time, in <a href=\\\"http://www.iso.org/iso/iso8601\\\">ISO 8601 date-time </a> format, when the private key was uploaded.",
          "type" : "string",
          "format" : "date-time"
        }
      },
      "required" : [ "KeyId", "Timestamp" ]
    }
  },
  "createOnlyProperties" : [ "/properties/Name", "/properties/AddPrivateKey", "/properties/RemovePrivateKey" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/SamlProviderUUID" ],
  "writeOnlyProperties" : [ "/properties/AddPrivateKey", "/properties/RemovePrivateKey" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:CreateSAMLProvider", "iam:GetSAMLProvider", "iam:TagSAMLProvider" ]
    },
    "read" : {
      "permissions" : [ "iam:GetSAMLProvider" ]
    },
    "update" : {
      "permissions" : [ "iam:UpdateSAMLProvider", "iam:GetSAMLProvider", "iam:TagSAMLProvider", "iam:ListSAMLProviderTags", "iam:UntagSAMLProvider" ]
    },
    "delete" : {
      "permissions" : [ "iam:DeleteSAMLProvider" ]
    },
    "list" : {
      "permissions" : [ "iam:ListSAMLProviders", "iam:GetSAMLProvider" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iam:TagSAMLProvider", "iam:ListSAMLProviderTags", "iam:UntagSAMLProvider" ]
  }
}