SCHEMA = {
  "typeName" : "AWS::Neptune::DBParameterGroup",
  "description" : "AWS::Neptune::DBParameterGroup creates a new DB parameter group. This type can be declared in a template and referenced in the DBParameterGroupName parameter of AWS::Neptune::DBInstance",
  "additionalProperties" : False,
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-neptune",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -."
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -."
        }
      },
      "additionalProperties" : False,
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "Name" : {
      "description" : "Provides the name of the DB parameter group.",
      "type" : "string"
    },
    "Description" : {
      "description" : "Provides the customer-specified description for this DB parameter group.",
      "type" : "string"
    },
    "Family" : {
      "description" : "Must be `neptune1` for engine versions prior to 1.2.0.0, or `neptune1.2` for engine version `1.2.0.0` and higher.",
      "type" : "string"
    },
    "Parameters" : {
      "description" : "The parameters to set for this DB parameter group.\n\nThe parameters are expressed as a JSON object consisting of key-value pairs.\n\nChanges to dynamic parameters are applied immediately. During an update, if you have static parameters (whether they were changed or not), it triggers AWS CloudFormation to reboot the associated DB instance without failover.",
      "type" : "object"
    },
    "Tags" : {
      "description" : "An optional array of key-value pairs to apply to this DB parameter group.",
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "propertyTransform" : {
    "/properties/Name" : "$lowercase(Name)"
  },
  "required" : [ "Family", "Description", "Parameters" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "rds:AddTagsToResource", "rds:ListTagsForResource", "rds:RemoveTagsFromResource" ]
  },
  "createOnlyProperties" : [ "/properties/Name", "/properties/Description", "/properties/Family" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "rds:AddTagsToResource", "rds:CreateDBParameterGroup", "rds:DescribeDBParameterGroups", "rds:DescribeDBParameters", "rds:DescribeEngineDefaultParameters", "rds:ModifyDBParameterGroup", "rds:ListTagsForResource", "iam:CreateServiceLinkedRole" ]
    },
    "read" : {
      "permissions" : [ "rds:DescribeDBParameterGroups", "rds:ListTagsForResource", "rds:DescribeDBParameters", "rds:DescribeEngineDefaultParameters" ]
    },
    "update" : {
      "permissions" : [ "rds:AddTagsToResource", "rds:DescribeDBParameterGroups", "rds:DescribeDBParameters", "rds:DescribeEngineDefaultParameters", "rds:ListTagsForResource", "rds:ModifyDBParameterGroup", "rds:ResetDBParameterGroup", "rds:RemoveTagsFromResource", "rds:DescribeDBInstances" ]
    },
    "delete" : {
      "permissions" : [ "rds:DeleteDBParameterGroup", "rds:RemoveTagsFromResource" ]
    },
    "list" : {
      "permissions" : [ "rds:DescribeDBParameterGroups", "rds:ListTagsForResource" ]
    }
  }
}