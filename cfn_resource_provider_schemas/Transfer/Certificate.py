SCHEMA = {
  "typeName" : "AWS::Transfer::Certificate",
  "description" : "Resource Type definition for AWS::Transfer::Certificate",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Usage" : {
      "description" : "Specifies the usage type for the certificate.",
      "type" : "string",
      "enum" : [ "SIGNING", "ENCRYPTION", "TLS" ]
    },
    "Certificate" : {
      "description" : "Specifies the certificate body to be imported.",
      "type" : "string",
      "pattern" : "^[\\t\\n\\r\\u0020-\\u00FF]+$",
      "minLength" : 1,
      "maxLength" : 16384
    },
    "CertificateChain" : {
      "description" : "Specifies the certificate chain to be imported.",
      "type" : "string",
      "pattern" : "^[\\t\\n\\r\\u0020-\\u00FF]+$",
      "minLength" : 1,
      "maxLength" : 2097152
    },
    "PrivateKey" : {
      "description" : "Specifies the private key for the certificate.",
      "type" : "string",
      "pattern" : "^[\\t\\n\\r\\u0020-\\u00FF]+$",
      "minLength" : 1,
      "maxLength" : 16384
    },
    "ActiveDate" : {
      "description" : "Specifies the active date for the certificate.",
      "type" : "string"
    },
    "InactiveDate" : {
      "description" : "Specifies the inactive date for the certificate.",
      "type" : "string"
    },
    "Description" : {
      "description" : "A textual description for the certificate.",
      "type" : "string",
      "pattern" : "^[\\u0021-\\u007E]+$",
      "minLength" : 1,
      "maxLength" : 200
    },
    "Tags" : {
      "description" : "Key-value pairs that can be used to group and search for certificates. Tags are metadata attached to certificates for any purpose.",
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Arn" : {
      "description" : "Specifies the unique Amazon Resource Name (ARN) for the agreement.",
      "type" : "string",
      "pattern" : "arn:.*",
      "minLength" : 20,
      "maxLength" : 1600
    },
    "CertificateId" : {
      "description" : "A unique identifier for the certificate.",
      "type" : "string",
      "pattern" : "^cert-([0-9a-f]{17})$",
      "minLength" : 22,
      "maxLength" : 22
    },
    "Status" : {
      "description" : "A status description for the certificate.",
      "type" : "string",
      "enum" : [ "ACTIVE", "PENDING", "INACTIVE" ]
    },
    "Type" : {
      "description" : "Describing the type of certificate. With or without a private key.",
      "type" : "string",
      "enum" : [ "CERTIFICATE", "CERTIFICATE_WITH_PRIVATE_KEY" ]
    },
    "Serial" : {
      "description" : "Specifies Certificate's serial.",
      "type" : "string",
      "pattern" : "^[0-9a-fA-F{}:?]*$",
      "minLength" : 0,
      "maxLength" : 48
    },
    "NotBeforeDate" : {
      "description" : "Specifies the not before date for the certificate.",
      "type" : "string"
    },
    "NotAfterDate" : {
      "description" : "Specifies the not after date for the certificate.",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "Certificate", "Usage" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CertificateId", "/properties/Status", "/properties/Type", "/properties/Serial", "/properties/NotAfterDate", "/properties/NotBeforeDate" ],
  "writeOnlyProperties" : [ "/properties/PrivateKey" ],
  "createOnlyProperties" : [ "/properties/Certificate", "/properties/CertificateChain", "/properties/PrivateKey" ],
  "primaryIdentifier" : [ "/properties/CertificateId" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "transfer:ListTagsForResource", "transfer:UnTagResource", "transfer:TagResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "transfer:ImportCertificate", "transfer:TagResource" ]
    },
    "read" : {
      "permissions" : [ "transfer:DescribeCertificate" ]
    },
    "update" : {
      "permissions" : [ "transfer:UpdateCertificate", "transfer:UnTagResource", "transfer:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "transfer:DeleteCertificate" ]
    },
    "list" : {
      "permissions" : [ "transfer:ListCertificates" ]
    }
  }
}