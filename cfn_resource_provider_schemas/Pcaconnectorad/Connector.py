SCHEMA = {
  "typeName" : "AWS::PCAConnectorAD::Connector",
  "description" : "Represents a Connector that connects AWS PrivateCA and your directory",
  "definitions" : {
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
    },
    "VpcInformation" : {
      "type" : "object",
      "properties" : {
        "SecurityGroupIds" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 20,
            "minLength" : 11,
            "pattern" : "^(?:sg-[0-9a-f]{8}|sg-[0-9a-f]{17})$"
          },
          "maxItems" : 5,
          "minItems" : 1,
          "uniqueItems" : True
        },
        "IpAddressType" : {
          "type" : "string",
          "enum" : [ "IPV4", "DUALSTACK" ]
        }
      },
      "required" : [ "SecurityGroupIds" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "CertificateAuthorityArn" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 5,
      "pattern" : "^arn:[\\w-]+:acm-pca:[\\w-]+:[0-9]+:certificate-authority\\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$"
    },
    "ConnectorArn" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 5,
      "pattern" : "^arn:[\\w-]+:pca-connector-ad:[\\w-]+:[0-9]+:connector\\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$"
    },
    "DirectoryId" : {
      "type" : "string",
      "pattern" : "^d-[0-9a-f]{10}$"
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    },
    "VpcInformation" : {
      "$ref" : "#/definitions/VpcInformation"
    }
  },
  "required" : [ "CertificateAuthorityArn", "DirectoryId", "VpcInformation" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "pca-connector-ad:ListTagsForResource", "pca-connector-ad:TagResource", "pca-connector-ad:UntagResource" ]
  },
  "readOnlyProperties" : [ "/properties/ConnectorArn" ],
  "createOnlyProperties" : [ "/properties/CertificateAuthorityArn", "/properties/DirectoryId", "/properties/VpcInformation" ],
  "primaryIdentifier" : [ "/properties/ConnectorArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "acm-pca:DescribeCertificateAuthority", "acm-pca:GetCertificateAuthorityCertificate", "acm-pca:GetCertificate", "acm-pca:IssueCertificate", "ds:DescribeDirectories", "ec2:CreateTags", "ec2:CreateVpcEndpoint", "ec2:DescribeVpcEndpoints", "pca-connector-ad:CreateConnector", "pca-connector-ad:GetConnector", "pca-connector-ad:TagResource" ]
    },
    "read" : {
      "permissions" : [ "pca-connector-ad:ListTagsForResource", "pca-connector-ad:GetConnector" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteVpcEndpoints", "ec2:DescribeVpcEndpoints", "pca-connector-ad:GetConnector", "pca-connector-ad:DeleteConnector", "pca-connector-ad:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "pca-connector-ad:ListConnectors" ]
    },
    "update" : {
      "permissions" : [ "pca-connector-ad:ListTagsForResource", "pca-connector-ad:TagResource", "pca-connector-ad:UntagResource" ]
    }
  },
  "additionalProperties" : False
}