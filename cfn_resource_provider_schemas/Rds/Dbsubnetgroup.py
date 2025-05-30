SCHEMA = {
  "typeName" : "AWS::RDS::DBSubnetGroup",
  "description" : "The ``AWS::RDS::DBSubnetGroup`` resource creates a database subnet group. Subnet groups must contain at least two subnets in two different Availability Zones in the same region. \n For more information, see [Working with DB subnet groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Subnets) in the *Amazon RDS User Guide*.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-rds",
  "properties" : {
    "DBSubnetGroupDescription" : {
      "type" : "string",
      "description" : "The description for the DB subnet group."
    },
    "DBSubnetGroupName" : {
      "type" : "string",
      "description" : "The name for the DB subnet group. This value is stored as a lowercase string.\n Constraints:\n  +  Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens.\n  +  Must not be default.\n  +  First character must be a letter.\n  \n Example: ``mydbsubnetgroup``"
    },
    "SubnetIds" : {
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      },
      "description" : "The EC2 Subnet IDs for the DB subnet group."
    },
    "Tags" : {
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : False,
      "insertionOrder" : False,
      "description" : "Tags to assign to the DB subnet group.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "Tag" : {
      "description" : "Metadata assigned to an Amazon RDS resource consisting of a key-value pair.\n For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with ``aws:`` or ``rds:``. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', ':', '/', '=', '+', '-', '@' (Java regex: \"^([\\\\p{L}\\\\p{Z}\\\\p{N}_.:/=+\\\\-@]*)$\").",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with ``aws:`` or ``rds:``. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', ':', '/', '=', '+', '-', '@' (Java regex: \"^([\\\\p{L}\\\\p{Z}\\\\p{N}_.:/=+\\\\-@]*)$\").",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key" ]
    }
  },
  "additionalProperties" : False,
  "required" : [ "DBSubnetGroupDescription", "SubnetIds" ],
  "propertyTransform" : {
    "/properties/DBSubnetGroupName" : "$lowercase(DBSubnetGroupName)"
  },
  "createOnlyProperties" : [ "/properties/DBSubnetGroupName" ],
  "primaryIdentifier" : [ "/properties/DBSubnetGroupName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:CreateServiceLinkedRole", "rds:CreateDBSubnetGroup", "rds:DescribeDBSubnetGroups", "rds:AddTagsToResource", "rds:RemoveTagsFromResource", "rds:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "rds:DescribeDBSubnetGroups", "rds:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "rds:ModifyDBSubnetGroup", "rds:DescribeDBSubnetGroups", "rds:AddTagsToResource", "rds:RemoveTagsFromResource", "rds:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "rds:DeleteDBSubnetGroup", "rds:DescribeDBSubnetGroups", "rds:ListTagsForResource" ]
    },
    "list" : {
      "permissions" : [ "rds:DescribeDBSubnetGroups" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "rds:AddTagsToResource", "rds:RemoveTagsFromResource" ]
  }
}