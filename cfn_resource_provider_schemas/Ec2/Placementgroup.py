SCHEMA = {
  "typeName" : "AWS::EC2::PlacementGroup",
  "description" : "Resource Type definition for AWS::EC2::PlacementGroup",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2",
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
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Strategy" : {
      "description" : "The placement strategy.",
      "type" : "string"
    },
    "GroupName" : {
      "description" : "The Group Name of Placement Group.",
      "type" : "string"
    },
    "SpreadLevel" : {
      "description" : "The Spread Level of Placement Group is an enum where it accepts either host or rack when strategy is spread",
      "type" : "string"
    },
    "PartitionCount" : {
      "description" : "The number of partitions. Valid only when **Strategy** is set to `partition`",
      "type" : "integer"
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
  "createOnlyProperties" : [ "/properties/Tags", "/properties/Strategy", "/properties/SpreadLevel", "/properties/PartitionCount" ],
  "primaryIdentifier" : [ "/properties/GroupName" ],
  "readOnlyProperties" : [ "/properties/GroupName" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ec2:CreateTags" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreatePlacementGroup", "ec2:DescribePlacementGroups", "ec2:CreateTags" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribePlacementGroups" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeletePlacementGroup", "ec2:DescribePlacementGroups" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribePlacementGroups" ]
    }
  }
}