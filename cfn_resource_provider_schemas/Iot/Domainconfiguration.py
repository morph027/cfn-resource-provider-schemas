SCHEMA = {
  "typeName" : "AWS::IoT::DomainConfiguration",
  "description" : "Create and manage a Domain Configuration",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "AuthorizerConfig" : {
      "type" : "object",
      "properties" : {
        "AllowAuthorizerOverride" : {
          "type" : "boolean"
        },
        "DefaultAuthorizerName" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128,
          "pattern" : "^[\\w=,@-]+$"
        }
      },
      "additionalProperties" : False
    },
    "ServerCertificateConfig" : {
      "type" : "object",
      "properties" : {
        "EnableOCSPCheck" : {
          "type" : "boolean"
        },
        "OcspLambdaArn" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 170
        },
        "OcspAuthorizedResponderArn" : {
          "type" : "string",
          "pattern" : "^arn:aws(-cn|-us-gov|-iso-b|-iso)?:acm:[a-z]{2}-(gov-|iso-|isob-)?[a-z]{4,9}-\\d{1}:\\d{12}:certificate/[a-zA-Z0-9/-]+$",
          "minLength" : 1,
          "maxLength" : 2048
        }
      },
      "additionalProperties" : False
    },
    "ServerCertificateSummary" : {
      "type" : "object",
      "properties" : {
        "ServerCertificateArn" : {
          "type" : "string",
          "pattern" : "^arn:aws(-cn|-us-gov|-iso-b|-iso)?:acm:[a-z]{2}-(gov-|iso-|isob-)?[a-z]{4,9}-\\d{1}:\\d{12}:certificate/[a-zA-Z0-9/-]+$",
          "minLength" : 1,
          "maxLength" : 2048
        },
        "ServerCertificateStatus" : {
          "type" : "string",
          "enum" : [ "INVALID", "VALID" ]
        },
        "ServerCertificateStatusDetail" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "TlsConfig" : {
      "type" : "object",
      "properties" : {
        "SecurityPolicy" : {
          "type" : "string",
          "maxLength" : 128
        }
      },
      "additionalProperties" : False
    },
    "ClientCertificateConfig" : {
      "type" : "object",
      "properties" : {
        "ClientCertificateCallbackArn" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 170
        }
      },
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False,
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "DomainConfigurationName" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "^[\\w.-]+$"
    },
    "AuthorizerConfig" : {
      "$ref" : "#/definitions/AuthorizerConfig"
    },
    "DomainName" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 253
    },
    "ServerCertificateArns" : {
      "type" : "array",
      "minItems" : 0,
      "maxItems" : 1,
      "insertionOrder" : True,
      "items" : {
        "type" : "string",
        "pattern" : "^arn:aws(-cn|-us-gov|-iso-b|-iso)?:acm:[a-z]{2}-(gov-|iso-|isob-)?[a-z]{4,9}-\\d{1}:\\d{12}:certificate/[a-zA-Z0-9/-]+$",
        "minLength" : 1,
        "maxLength" : 2048
      }
    },
    "ServiceType" : {
      "type" : "string",
      "enum" : [ "DATA", "CREDENTIAL_PROVIDER", "JOBS" ]
    },
    "ValidationCertificateArn" : {
      "type" : "string",
      "pattern" : "^arn:aws(-cn|-us-gov|-iso-b|-iso)?:acm:[a-z]{2}-(gov-|iso-|isob-)?[a-z]{4,9}-\\d{1}:\\d{12}:certificate/[a-zA-Z0-9/-]+$"
    },
    "Arn" : {
      "type" : "string"
    },
    "DomainConfigurationStatus" : {
      "type" : "string",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "DomainType" : {
      "type" : "string",
      "enum" : [ "ENDPOINT", "AWS_MANAGED", "CUSTOMER_MANAGED" ]
    },
    "ServerCertificateConfig" : {
      "$ref" : "#/definitions/ServerCertificateConfig"
    },
    "ServerCertificates" : {
      "type" : "array",
      "insertionOrder" : True,
      "items" : {
        "$ref" : "#/definitions/ServerCertificateSummary"
      }
    },
    "TlsConfig" : {
      "$ref" : "#/definitions/TlsConfig"
    },
    "AuthenticationType" : {
      "type" : "string",
      "enum" : [ "AWS_X509", "CUSTOM_AUTH", "AWS_SIGV4", "CUSTOM_AUTH_X509", "DEFAULT" ]
    },
    "ApplicationProtocol" : {
      "type" : "string",
      "enum" : [ "SECURE_MQTT", "MQTT_WSS", "HTTPS", "DEFAULT" ]
    },
    "ClientCertificateConfig" : {
      "$ref" : "#/definitions/ClientCertificateConfig"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iot:ListTagsForResource", "iot:TagResource", "iot:UntagResource" ]
  },
  "additionalProperties" : False,
  "required" : [ ],
  "createOnlyProperties" : [ "/properties/DomainConfigurationName", "/properties/DomainName", "/properties/ServiceType", "/properties/ValidationCertificateArn", "/properties/ServerCertificateArns" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/DomainType", "/properties/ServerCertificates" ],
  "writeOnlyProperties" : [ "/properties/ValidationCertificateArn", "/properties/ServerCertificateArns" ],
  "primaryIdentifier" : [ "/properties/DomainConfigurationName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iot:CreateDomainConfiguration", "iot:UpdateDomainConfiguration", "iot:DescribeDomainConfiguration", "iot:TagResource", "iot:ListTagsForResource", "acm:GetCertificate" ]
    },
    "read" : {
      "permissions" : [ "iot:DescribeDomainConfiguration", "iot:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iot:UpdateDomainConfiguration", "iot:DescribeDomainConfiguration", "iot:ListTagsForResource", "iot:TagResource", "iot:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "iot:DescribeDomainConfiguration", "iot:DeleteDomainConfiguration", "iot:UpdateDomainConfiguration" ]
    },
    "list" : {
      "permissions" : [ "iot:ListDomainConfigurations" ]
    }
  }
}