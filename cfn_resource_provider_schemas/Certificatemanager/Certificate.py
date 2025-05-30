SCHEMA = {
  "typeName" : "AWS::CertificateManager::Certificate",
  "description" : "Resource Type definition for AWS::CertificateManager::Certificate",
  "additionalProperties" : False,
  "properties" : {
    "CertificateAuthorityArn" : {
      "type" : "string"
    },
    "DomainValidationOptions" : {
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/DomainValidationOption"
      }
    },
    "CertificateTransparencyLoggingPreference" : {
      "type" : "string"
    },
    "DomainName" : {
      "type" : "string"
    },
    "ValidationMethod" : {
      "type" : "string"
    },
    "SubjectAlternativeNames" : {
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "type" : "string"
      }
    },
    "Id" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "KeyAlgorithm" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "DomainValidationOption" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DomainName" : {
          "type" : "string"
        },
        "ValidationDomain" : {
          "type" : "string"
        },
        "HostedZoneId" : {
          "type" : "string"
        }
      },
      "required" : [ "DomainName" ]
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "required" : [ "DomainName" ],
  "createOnlyProperties" : [ "/properties/SubjectAlternativeNames", "/properties/DomainValidationOptions", "/properties/ValidationMethod", "/properties/KeyAlgorithm", "/properties/DomainName", "/properties/CertificateAuthorityArn" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}