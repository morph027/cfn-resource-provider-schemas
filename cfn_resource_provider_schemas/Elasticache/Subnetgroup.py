SCHEMA = {
  "typeName" : "AWS::ElastiCache::SubnetGroup",
  "description" : "Resource Type definition for AWS::ElastiCache::SubnetGroup",
  "properties" : {
    "Description" : {
      "type" : "string",
      "description" : "The description for the cache subnet group."
    },
    "SubnetIds" : {
      "description" : "The EC2 subnet IDs for the cache subnet group.",
      "type" : "array",
      "items" : {
        "type" : "string"
      },
      "insertionOrder" : False,
      "uniqueItems" : False
    },
    "CacheSubnetGroupName" : {
      "type" : "string",
      "description" : "The name for the cache subnet group. This value is stored as a lowercase string."
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "description" : "A tag that can be added to an ElastiCache subnet group. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your subnet groups. A tag with a None Value is permitted.",
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
  "required" : [ "Description", "SubnetIds" ],
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/CacheSubnetGroupName" ],
  "primaryIdentifier" : [ "/properties/CacheSubnetGroupName" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "elasticache:CreateCacheSubnetGroup", "elasticache:AddTagsToResource", "elasticache:DescribeCacheSubnetGroups", "elasticache:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "elasticache:DescribeCacheSubnetGroups", "elasticache:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "elasticache:DeleteCacheSubnetGroup", "elasticache:DescribeCacheSubnetGroups", "elasticache:ListTagsForResource" ]
    },
    "list" : {
      "permissions" : [ "elasticache:DescribeCacheSubnetGroups" ]
    },
    "update" : {
      "permissions" : [ "elasticache:ModifyCacheSubnetGroup", "elasticache:DescribeCacheSubnetGroups", "elasticache:AddTagsToResource", "elasticache:RemoveTagsFromResource" ]
    }
  }
}