SCHEMA = {
  "typeName" : "AWS::DMS::ReplicationConfig",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-dms",
  "description" : "A replication configuration that you later provide to configure and start a AWS DMS Serverless replication",
  "definitions" : {
    "ComputeConfig" : {
      "description" : "Configuration parameters for provisioning a AWS DMS Serverless replication",
      "type" : "object",
      "properties" : {
        "AvailabilityZone" : {
          "type" : "string"
        },
        "DnsNameServers" : {
          "type" : "string"
        },
        "KmsKeyId" : {
          "type" : "string"
        },
        "MaxCapacityUnits" : {
          "type" : "integer"
        },
        "MinCapacityUnits" : {
          "type" : "integer"
        },
        "MultiAZ" : {
          "type" : "boolean"
        },
        "PreferredMaintenanceWindow" : {
          "type" : "string"
        },
        "ReplicationSubnetGroupId" : {
          "type" : "string"
        },
        "VpcSecurityGroupIds" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        }
      },
      "required" : [ "MaxCapacityUnits" ],
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "description" : "<p>The key or keys of the key-value pairs for the resource tag or tags assigned to the\n            resource.</p>",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "description" : "<p>Tag key.</p>"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "description" : "<p>Tag value.</p>"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ReplicationConfigIdentifier" : {
      "description" : "A unique identifier of replication configuration",
      "type" : "string"
    },
    "ReplicationConfigArn" : {
      "description" : "The Amazon Resource Name (ARN) of the Replication Config",
      "type" : "string"
    },
    "SourceEndpointArn" : {
      "description" : "The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration",
      "type" : "string"
    },
    "TargetEndpointArn" : {
      "description" : "The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS Serverless replication configuration",
      "type" : "string"
    },
    "ReplicationType" : {
      "description" : "The type of AWS DMS Serverless replication to provision using this replication configuration",
      "type" : "string",
      "enum" : [ "full-load", "full-load-and-cdc", "cdc" ]
    },
    "ComputeConfig" : {
      "$ref" : "#/definitions/ComputeConfig"
    },
    "ReplicationSettings" : {
      "description" : "JSON settings for Servereless replications that are provisioned using this replication configuration",
      "type" : "object"
    },
    "SupplementalSettings" : {
      "description" : "JSON settings for specifying supplemental data",
      "type" : "object"
    },
    "ResourceIdentifier" : {
      "description" : "A unique value or name that you get set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource",
      "type" : "string"
    },
    "TableMappings" : {
      "description" : "JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration",
      "type" : "object"
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 200,
      "minItems" : 1,
      "description" : "<p>Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.</p>"
    }
  },
  "createOnlyProperties" : [ "/properties/ResourceIdentifier" ],
  "readOnlyProperties" : [ "/properties/ReplicationConfigArn" ],
  "primaryIdentifier" : [ "/properties/ReplicationConfigArn" ],
  "additionalIdentifiers" : [ [ "/properties/ReplicationConfigIdentifier" ] ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "dms:AddTagsToResource", "dms:ListTagsForResource", "dms:RemoveTagsFromResource" ]
  },
  "additionalProperties" : False,
  "required" : [ "ReplicationConfigIdentifier", "SourceEndpointArn", "TargetEndpointArn", "ReplicationType", "ComputeConfig", "TableMappings" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "dms:CreateReplicationConfig", "dms:AddTagsToResource", "dms:ListTagsForResource", "iam:CreateServiceLinkedRole", "iam:AttachRolePolicy", "iam:PutRolePolicy", "iam:UpdateRoleDescription" ]
    },
    "read" : {
      "permissions" : [ "dms:DescribeReplicationConfigs", "dms:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "dms:ModifyReplicationConfig", "dms:AddTagsToResource", "dms:RemoveTagsFromResource", "dms:ListTagsForResource", "iam:CreateServiceLinkedRole", "iam:AttachRolePolicy", "iam:PutRolePolicy", "iam:UpdateRoleDescription" ]
    },
    "list" : {
      "permissions" : [ "dms:DescribeReplicationConfigs", "dms:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "dms:DescribeReplicationConfigs", "dms:DeleteReplicationConfig", "dms:ListTagsForResource", "iam:DeleteServiceLinkedRole", "iam:GetServiceLinkedRoleDeletionStatus" ]
    }
  }
}