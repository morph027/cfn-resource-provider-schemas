SCHEMA = {
  "typeName" : "AWS::RDS::OptionGroup",
  "description" : "The ``AWS::RDS::OptionGroup`` resource creates or updates an option group, to enable and configure features that are specific to a particular DB engine.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-rds",
  "definitions" : {
    "OptionConfiguration" : {
      "description" : "The ``OptionConfiguration`` property type specifies an individual option, and its settings, within an ``AWS::RDS::OptionGroup`` resource.",
      "type" : "object",
      "properties" : {
        "DBSecurityGroupMemberships" : {
          "description" : "A list of DB security groups used for this option.",
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "items" : {
            "type" : "string"
          }
        },
        "OptionName" : {
          "description" : "The configuration of options to include in a group.",
          "type" : "string"
        },
        "OptionSettings" : {
          "description" : "The option settings to include in an option group.",
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/OptionSetting"
          }
        },
        "OptionVersion" : {
          "description" : "The version for the option.",
          "type" : "string"
        },
        "Port" : {
          "description" : "The optional port for the option.",
          "type" : "integer"
        },
        "VpcSecurityGroupMemberships" : {
          "description" : "A list of VPC security group names used for this option.",
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "items" : {
            "type" : "string"
          }
        }
      },
      "additionalProperties" : False,
      "required" : [ "OptionName" ]
    },
    "OptionSetting" : {
      "description" : "The ``OptionSetting`` property type specifies the value for an option within an ``OptionSetting`` property.",
      "type" : "object",
      "properties" : {
        "Name" : {
          "description" : "The name of the option that has settings that you can set.",
          "type" : "string"
        },
        "Value" : {
          "description" : "The current value of the option setting.",
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
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
  "properties" : {
    "OptionGroupName" : {
      "description" : "The name of the option group to be created.\n Constraints:\n  +  Must be 1 to 255 letters, numbers, or hyphens\n  +  First character must be a letter\n  +  Can't end with a hyphen or contain two consecutive hyphens\n  \n Example: ``myoptiongroup``\n If you don't specify a value for ``OptionGroupName`` property, a name is automatically created for the option group.\n  This value is stored as a lowercase string.",
      "type" : "string"
    },
    "OptionGroupDescription" : {
      "description" : "The description of the option group.",
      "type" : "string"
    },
    "EngineName" : {
      "description" : "Specifies the name of the engine that this option group should be associated with.\n Valid Values: \n  +   ``mariadb`` \n  +   ``mysql`` \n  +   ``oracle-ee`` \n  +   ``oracle-ee-cdb`` \n  +   ``oracle-se2`` \n  +   ``oracle-se2-cdb`` \n  +   ``postgres`` \n  +   ``sqlserver-ee`` \n  +   ``sqlserver-se`` \n  +   ``sqlserver-ex`` \n  +   ``sqlserver-web``",
      "type" : "string"
    },
    "MajorEngineVersion" : {
      "description" : "Specifies the major version of the engine that this option group should be associated with.",
      "type" : "string"
    },
    "OptionConfigurations" : {
      "description" : "A list of all available options for an option group.",
      "type" : "array",
      "arrayType" : "AttributeList",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/OptionConfiguration"
      }
    },
    "Tags" : {
      "type" : "array",
      "description" : "Tags to assign to the option group.",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "propertyTransform" : {
    "/properties/OptionGroupName" : "$lowercase(OptionGroupName)"
  },
  "required" : [ "EngineName", "MajorEngineVersion", "OptionGroupDescription" ],
  "createOnlyProperties" : [ "/properties/EngineName", "/properties/MajorEngineVersion", "/properties/OptionGroupDescription", "/properties/OptionGroupName" ],
  "primaryIdentifier" : [ "/properties/OptionGroupName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:CreateServiceLinkedRole", "rds:AddTagsToResource", "rds:CreateOptionGroup", "rds:DescribeOptionGroups", "rds:ListTagsForResource", "rds:ModifyOptionGroup", "rds:RemoveTagsFromResource" ]
    },
    "read" : {
      "permissions" : [ "rds:DescribeOptionGroups", "rds:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "rds:AddTagsToResource", "rds:DescribeOptionGroups", "rds:ListTagsForResource", "rds:ModifyOptionGroup", "rds:RemoveTagsFromResource" ]
    },
    "delete" : {
      "permissions" : [ "rds:DeleteOptionGroup", "rds:DescribeOptionGroups", "rds:ListTagsForResource", "rds:RemoveTagsFromResource" ]
    },
    "list" : {
      "permissions" : [ "rds:DescribeOptionGroups" ]
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