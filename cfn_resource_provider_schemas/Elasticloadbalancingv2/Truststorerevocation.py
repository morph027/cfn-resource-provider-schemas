SCHEMA = {
  "typeName" : "AWS::ElasticLoadBalancingV2::TrustStoreRevocation",
  "description" : "Resource Type definition for AWS::ElasticLoadBalancingV2::TrustStoreRevocation",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-elasticloadbalancingv2",
  "documentationUrl" : "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-truststorerevocation.html",
  "additionalProperties" : False,
  "properties" : {
    "RevocationContents" : {
      "type" : "array",
      "description" : "The attributes required to create a trust store revocation.",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/RevocationContent"
      }
    },
    "TrustStoreArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the trust store."
    },
    "RevocationId" : {
      "type" : "integer",
      "format" : "int64",
      "description" : "The ID associated with the revocation."
    },
    "TrustStoreRevocations" : {
      "type" : "array",
      "description" : "The data associated with a trust store revocation",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/TrustStoreRevocation"
      }
    }
  },
  "definitions" : {
    "RevocationId" : {
      "type" : "string"
    },
    "RevocationContent" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "S3Bucket" : {
          "type" : "string"
        },
        "S3Key" : {
          "type" : "string"
        },
        "S3ObjectVersion" : {
          "type" : "string"
        },
        "RevocationType" : {
          "type" : "string"
        }
      }
    },
    "TrustStoreRevocation" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TrustStoreArn" : {
          "type" : "string"
        },
        "RevocationId" : {
          "type" : "string"
        },
        "RevocationType" : {
          "type" : "string"
        },
        "NumberOfRevokedEntries" : {
          "type" : "integer",
          "format" : "int64"
        }
      }
    }
  },
  "primaryIdentifier" : [ "/properties/RevocationId", "/properties/TrustStoreArn" ],
  "createOnlyProperties" : [ "/properties/TrustStoreArn", "/properties/RevocationContents" ],
  "writeOnlyProperties" : [ "/properties/RevocationContents" ],
  "readOnlyProperties" : [ "/properties/RevocationId", "/properties/TrustStoreRevocations" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "elasticloadbalancing:AddTrustStoreRevocations", "elasticloadbalancing:DescribeTrustStoreRevocations", "s3:GetObject", "s3:GetObjectVersion" ]
    },
    "delete" : {
      "permissions" : [ "elasticloadbalancing:DescribeTrustStoreRevocations", "elasticloadbalancing:RemoveTrustStoreRevocations" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "TrustStoreArn" : {
            "$ref" : "resource-schema.json#/properties/TrustStoreArn"
          },
          "RevocationIds" : {
            "type" : "array",
            "uniqueItems" : False,
            "insertionOrder" : False,
            "items" : {
              "$ref" : "resource-schema.json#/properties/RevocationId"
            }
          }
        },
        "required" : [ "TrustStoreArn" ]
      },
      "permissions" : [ "elasticloadbalancing:DescribeTrustStoreRevocations" ]
    },
    "read" : {
      "permissions" : [ "elasticloadbalancing:DescribeTrustStoreRevocations" ]
    }
  }
}