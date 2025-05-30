SCHEMA = {
  "typeName" : "AWS::Lightsail::Certificate",
  "description" : "Resource Type definition for AWS::Lightsail::Certificate.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
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
      "required" : [ "Key" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "CertificateName" : {
      "description" : "The name for the certificate.",
      "type" : "string"
    },
    "DomainName" : {
      "description" : "The domain name (e.g., example.com ) for the certificate.",
      "type" : "string"
    },
    "SubjectAlternativeNames" : {
      "description" : "An array of strings that specify the alternate domains (e.g., example2.com) and subdomains (e.g., blog.example.com) for the certificate.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "CertificateArn" : {
      "type" : "string"
    },
    "Status" : {
      "description" : "The validation status of the certificate.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "CertificateName", "DomainName" ],
  "readOnlyProperties" : [ "/properties/CertificateArn", "/properties/Status" ],
  "primaryIdentifier" : [ "/properties/CertificateName" ],
  "createOnlyProperties" : [ "/properties/CertificateName", "/properties/DomainName", "/properties/SubjectAlternativeNames" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "lightsail:CreateCertificate", "lightsail:GetCertificates", "lightsail:TagResource", "lightsail:UntagResource" ]
    },
    "read" : {
      "permissions" : [ "lightsail:GetCertificates" ]
    },
    "update" : {
      "permissions" : [ "lightsail:GetCertificates", "lightsail:TagResource", "lightsail:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "lightsail:DeleteCertificate", "lightsail:GetCertificates" ]
    },
    "list" : {
      "permissions" : [ "lightsail:GetCertificates" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "lightsail:TagResource", "lightsail:UntagResource" ]
  }
}