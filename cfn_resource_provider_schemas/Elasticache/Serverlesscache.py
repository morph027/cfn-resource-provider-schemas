SCHEMA = {
  "typeName" : "AWS::ElastiCache::ServerlessCache",
  "description" : "The AWS::ElastiCache::ServerlessCache resource creates an Amazon ElastiCache Serverless Cache.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-elasticache",
  "definitions" : {
    "CacheUsageLimits" : {
      "description" : "The cache capacity limit of the Serverless Cache.",
      "type" : "object",
      "properties" : {
        "DataStorage" : {
          "$ref" : "#/definitions/DataStorage"
        },
        "ECPUPerSecond" : {
          "$ref" : "#/definitions/ECPUPerSecond"
        }
      },
      "additionalProperties" : False
    },
    "DataStorage" : {
      "description" : "The cached data capacity of the Serverless Cache.",
      "type" : "object",
      "properties" : {
        "Minimum" : {
          "description" : "The minimum cached data capacity of the Serverless Cache.",
          "type" : "integer"
        },
        "Maximum" : {
          "description" : "The maximum cached data capacity of the Serverless Cache.",
          "type" : "integer"
        },
        "Unit" : {
          "description" : "The unit of cached data capacity of the Serverless Cache.",
          "type" : "string",
          "enum" : [ "GB" ]
        }
      },
      "additionalProperties" : False,
      "required" : [ "Unit" ]
    },
    "ECPUPerSecond" : {
      "description" : "The ECPU per second of the Serverless Cache.",
      "type" : "object",
      "properties" : {
        "Minimum" : {
          "description" : "The minimum ECPU per second of the Serverless Cache.",
          "type" : "integer"
        },
        "Maximum" : {
          "description" : "The maximum ECPU per second of the Serverless Cache.",
          "type" : "integer"
        }
      },
      "additionalProperties" : False
    },
    "Tag" : {
      "description" : "A key-value pair to associate with Serverless Cache.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:'. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string",
          "pattern" : "^(?!aws:)[a-zA-Z0-9 _\\.\\/=+:\\-@]*$",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9 _\\.\\/=+:\\-@]*$",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key" ]
    },
    "Endpoint" : {
      "description" : "The address and the port.",
      "type" : "object",
      "properties" : {
        "Address" : {
          "description" : "Endpoint address.",
          "type" : "string"
        },
        "Port" : {
          "description" : "Endpoint port.",
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ServerlessCacheName" : {
      "description" : "The name of the Serverless Cache. This value must be unique.",
      "type" : "string"
    },
    "Description" : {
      "description" : "The description of the Serverless Cache.",
      "type" : "string"
    },
    "Engine" : {
      "description" : "The engine name of the Serverless Cache.",
      "type" : "string"
    },
    "MajorEngineVersion" : {
      "description" : "The major engine version of the Serverless Cache.",
      "type" : "string"
    },
    "FullEngineVersion" : {
      "description" : "The full engine version of the Serverless Cache.",
      "type" : "string"
    },
    "CacheUsageLimits" : {
      "$ref" : "#/definitions/CacheUsageLimits"
    },
    "KmsKeyId" : {
      "description" : "The ID of the KMS key used to encrypt the cluster.",
      "type" : "string"
    },
    "SecurityGroupIds" : {
      "description" : "One or more Amazon VPC security groups associated with this Serverless Cache.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "SnapshotArnsToRestore" : {
      "description" : "The ARN's of snapshot to restore Serverless Cache.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this Serverless Cache.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "UserGroupId" : {
      "description" : "The ID of the user group.",
      "type" : "string"
    },
    "SubnetIds" : {
      "description" : "The subnet id's of the Serverless Cache.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "SnapshotRetentionLimit" : {
      "description" : "The snapshot retention limit of the Serverless Cache.",
      "type" : "integer"
    },
    "DailySnapshotTime" : {
      "description" : "The daily time range (in UTC) during which the service takes automatic snapshot of the Serverless Cache.",
      "type" : "string"
    },
    "CreateTime" : {
      "description" : "The creation time of the Serverless Cache.",
      "type" : "string"
    },
    "Status" : {
      "description" : "The status of the Serverless Cache.",
      "type" : "string"
    },
    "Endpoint" : {
      "$ref" : "#/definitions/Endpoint"
    },
    "ReaderEndpoint" : {
      "$ref" : "#/definitions/Endpoint"
    },
    "ARN" : {
      "description" : "The ARN of the Serverless Cache.",
      "type" : "string"
    },
    "FinalSnapshotName" : {
      "description" : "The final snapshot name which is taken before Serverless Cache is deleted.",
      "type" : "string"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "elasticache:AddTagsToResource", "elasticache:RemoveTagsFromResource" ]
  },
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/FullEngineVersion", "/properties/CreateTime", "/properties/Status", "/properties/Endpoint/Address", "/properties/Endpoint/Port", "/properties/ReaderEndpoint/Address", "/properties/ReaderEndpoint/Port", "/properties/ARN" ],
  "writeOnlyProperties" : [ "/properties/SnapshotArnsToRestore", "/properties/FinalSnapshotName" ],
  "createOnlyProperties" : [ "/properties/ServerlessCacheName", "/properties/KmsKeyId", "/properties/SnapshotArnsToRestore", "/properties/SubnetIds" ],
  "required" : [ "ServerlessCacheName", "Engine" ],
  "primaryIdentifier" : [ "/properties/ServerlessCacheName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "elasticache:CreateServerlessCache", "elasticache:DescribeServerlessCaches", "elasticache:AddTagsToResource", "elasticache:ListTagsForResource", "ec2:CreateTags", "ec2:CreateVpcEndpoint", "kms:CreateGrant", "kms:DescribeKey" ]
    },
    "read" : {
      "permissions" : [ "elasticache:DescribeServerlessCaches", "elasticache:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "elasticache:ModifyServerlessCache", "elasticache:DescribeServerlessCaches", "elasticache:AddTagsToResource", "elasticache:ListTagsForResource", "elasticache:RemoveTagsFromResource" ]
    },
    "delete" : {
      "permissions" : [ "elasticache:DeleteServerlessCache", "elasticache:DescribeServerlessCaches", "elasticache:ListTagsForResource" ]
    },
    "list" : {
      "permissions" : [ "elasticache:DescribeServerlessCaches", "elasticache:ListTagsForResource" ]
    }
  }
}