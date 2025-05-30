SCHEMA = {
  "typeName" : "AWS::ElasticLoadBalancingV2::TrustStore",
  "description" : "Resource Type definition for AWS::ElasticLoadBalancingV2::TrustStore",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-elasticloadbalancingv2",
  "documentationUrl" : "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-truststore.html",
  "additionalProperties" : False,
  "properties" : {
    "Name" : {
      "type" : "string",
      "description" : "The name of the trust store."
    },
    "CaCertificatesBundleS3Bucket" : {
      "type" : "string",
      "description" : "The name of the S3 bucket to fetch the CA certificate bundle from."
    },
    "CaCertificatesBundleS3Key" : {
      "type" : "string",
      "description" : "The name of the S3 object to fetch the CA certificate bundle from."
    },
    "CaCertificatesBundleS3ObjectVersion" : {
      "type" : "string",
      "description" : "The version of the S3 bucket that contains the CA certificate bundle."
    },
    "Status" : {
      "type" : "string",
      "description" : "The status of the trust store, could be either of ACTIVE or CREATING."
    },
    "NumberOfCaCertificates" : {
      "type" : "integer",
      "description" : "The number of certificates associated with the trust store."
    },
    "Tags" : {
      "type" : "array",
      "description" : "The tags to assign to the trust store.",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "TrustStoreArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the trust store."
    }
  },
  "definitions" : {
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
  "primaryIdentifier" : [ "/properties/TrustStoreArn" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "readOnlyProperties" : [ "/properties/TrustStoreArn", "/properties/Status", "/properties/NumberOfCaCertificates" ],
  "writeOnlyProperties" : [ "/properties/CaCertificatesBundleS3Bucket", "/properties/CaCertificatesBundleS3Key", "/properties/CaCertificatesBundleS3ObjectVersion" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "elasticloadbalancing:AddTags", "elasticloadbalancing:DescribeTags", "elasticloadbalancing:RemoveTags" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "elasticloadbalancing:CreateTrustStore", "elasticloadbalancing:DescribeTrustStores", "elasticloadbalancing:AddTags", "s3:GetObject", "s3:GetObjectVersion" ]
    },
    "delete" : {
      "permissions" : [ "elasticloadbalancing:DescribeTrustStores", "elasticloadbalancing:DeleteTrustStore" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "TrustStoreArns" : {
            "type" : "array",
            "uniqueItems" : False,
            "insertionOrder" : False,
            "items" : {
              "$ref" : "resource-schema.json#/properties/TrustStoreArn"
            }
          },
          "Names" : {
            "type" : "array",
            "uniqueItems" : False,
            "insertionOrder" : False,
            "items" : {
              "$ref" : "resource-schema.json#/properties/Name"
            }
          }
        }
      },
      "permissions" : [ "elasticloadbalancing:DescribeTrustStores", "s3:GetObject", "s3:GetObjectVersion" ]
    },
    "read" : {
      "permissions" : [ "elasticloadbalancing:DescribeTrustStores", "elasticloadbalancing:DescribeTags" ]
    },
    "update" : {
      "permissions" : [ "elasticloadbalancing:ModifyTrustStore", "elasticloadbalancing:AddTags", "elasticloadbalancing:RemoveTags", "s3:GetObject", "s3:GetObjectVersion" ]
    }
  }
}