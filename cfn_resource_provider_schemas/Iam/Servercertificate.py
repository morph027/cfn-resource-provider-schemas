SCHEMA = {
  "typeName" : "AWS::IAM::ServerCertificate",
  "description" : "Resource Type definition for AWS::IAM::ServerCertificate",
  "additionalProperties" : False,
  "properties" : {
    "CertificateBody" : {
      "minLength" : 1,
      "maxLength" : 16384,
      "pattern" : "[\\u0009\\u000A\\u000D\\u0020-\\u00FF]+",
      "type" : "string"
    },
    "CertificateChain" : {
      "minLength" : 1,
      "maxLength" : 2097152,
      "pattern" : "[\\u0009\\u000A\\u000D\\u0020-\\u00FF]+",
      "type" : "string"
    },
    "ServerCertificateName" : {
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "[\\w+=,.@-]+",
      "type" : "string"
    },
    "Path" : {
      "minLength" : 1,
      "maxLength" : 512,
      "pattern" : "(\\u002F)|(\\u002F[\\u0021-\\u007F]+\\u002F)",
      "type" : "string"
    },
    "PrivateKey" : {
      "minLength" : 1,
      "maxLength" : 16384,
      "pattern" : "[\\u0009\\u000A\\u000D\\u0020-\\u00FF]+",
      "type" : "string"
    },
    "Arn" : {
      "description" : "Amazon Resource Name (ARN) of the server certificate",
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
    }
  },
  "createOnlyProperties" : [ "/properties/ServerCertificateName", "/properties/PrivateKey", "/properties/CertificateBody", "/properties/CertificateChain" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "writeOnlyProperties" : [ "/properties/PrivateKey", "/properties/CertificateBody", "/properties/CertificateChain" ],
  "primaryIdentifier" : [ "/properties/ServerCertificateName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:UploadServerCertificate", "iam:TagServerCertificate", "iam:GetServerCertificate" ]
    },
    "read" : {
      "permissions" : [ "iam:GetServerCertificate" ]
    },
    "update" : {
      "permissions" : [ "iam:TagServerCertificate", "iam:UntagServerCertificate", "iam:ListServerCertificateTags", "iam:GetServerCertificate" ]
    },
    "delete" : {
      "permissions" : [ "iam:DeleteServerCertificate" ]
    },
    "list" : {
      "permissions" : [ "iam:ListServerCertificates", "iam:GetServerCertificate" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iam:TagServerCertificate", "iam:UntagServerCertificate", "iam:ListServerCertificateTags" ]
  }
}