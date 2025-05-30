SCHEMA = {
  "typeName" : "AWS::PCAConnectorSCEP::Connector",
  "description" : "Represents a Connector that allows certificate issuance through Simple Certificate Enrollment Protocol (SCEP)",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-pcaconnectorscep",
  "definitions" : {
    "ConnectorType" : {
      "type" : "string",
      "enum" : [ "GENERAL_PURPOSE", "INTUNE" ]
    },
    "IntuneConfiguration" : {
      "type" : "object",
      "properties" : {
        "AzureApplicationId" : {
          "type" : "string",
          "maxLength" : 100,
          "minLength" : 15,
          "pattern" : "^[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}-[a-zA-Z0-9]{2,15}$"
        },
        "Domain" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "pattern" : "^[a-zA-Z0-9._-]+$"
        }
      },
      "required" : [ "AzureApplicationId", "Domain" ],
      "additionalProperties" : False
    },
    "MobileDeviceManagement" : {
      "type" : "object",
      "oneOf" : [ {
        "title" : "Intune",
        "properties" : {
          "Intune" : {
            "$ref" : "#/definitions/IntuneConfiguration"
          }
        },
        "required" : [ "Intune" ],
        "additionalProperties" : False
      } ]
    },
    "OpenIdConfiguration" : {
      "type" : "object",
      "properties" : {
        "Issuer" : {
          "type" : "string"
        },
        "Subject" : {
          "type" : "string"
        },
        "Audience" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "Tags" : {
      "type" : "object",
      "patternProperties" : {
        ".+" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "Unit" : {
      "type" : "object",
      "additionalProperties" : False
    }
  },
  "properties" : {
    "CertificateAuthorityArn" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 5,
      "pattern" : "^arn:aws(-[a-z]+)*:acm-pca:[a-z]+(-[a-z]+)+-[1-9]\\d*:\\d{12}:certificate-authority\\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$"
    },
    "ConnectorArn" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 5,
      "pattern" : "^arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\\d*:\\d{12}:connector\\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$"
    },
    "Type" : {
      "$ref" : "#/definitions/ConnectorType"
    },
    "Endpoint" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 5
    },
    "MobileDeviceManagement" : {
      "$ref" : "#/definitions/MobileDeviceManagement"
    },
    "OpenIdConfiguration" : {
      "$ref" : "#/definitions/OpenIdConfiguration"
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "pca-connector-scep:ListTagsForResource", "pca-connector-scep:TagResource", "pca-connector-scep:UntagResource" ]
  },
  "required" : [ "CertificateAuthorityArn" ],
  "readOnlyProperties" : [ "/properties/ConnectorArn", "/properties/Endpoint", "/properties/OpenIdConfiguration", "/properties/Type" ],
  "createOnlyProperties" : [ "/properties/CertificateAuthorityArn", "/properties/MobileDeviceManagement" ],
  "primaryIdentifier" : [ "/properties/ConnectorArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "acm-pca:DescribeCertificateAuthority", "acm-pca:GetCertificate", "acm-pca:GetCertificateAuthorityCertificate", "acm-pca:IssueCertificate", "pca-connector-scep:GetConnector", "pca-connector-scep:CreateConnector", "pca-connector-scep:TagResource" ]
    },
    "read" : {
      "permissions" : [ "pca-connector-scep:ListTagsForResource", "pca-connector-scep:GetConnector" ]
    },
    "delete" : {
      "permissions" : [ "acm-pca:DescribeCertificateAuthority", "acm-pca:GetCertificate", "acm-pca:GetCertificateAuthorityCertificate", "acm-pca:IssueCertificate", "pca-connector-scep:GetConnector", "pca-connector-scep:DeleteConnector", "pca-connector-scep:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "pca-connector-scep:ListConnectors" ]
    },
    "update" : {
      "permissions" : [ "pca-connector-scep:ListTagsForResource", "pca-connector-scep:TagResource", "pca-connector-scep:UntagResource" ]
    }
  },
  "additionalProperties" : False
}