SCHEMA = {
  "typeName" : "AWS::Config::ConfigurationAggregator",
  "description" : "Resource Type definition for AWS::Config::ConfigurationAggregator",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-config.git",
  "additionalProperties" : False,
  "properties" : {
    "AccountAggregationSources" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/AccountAggregationSource"
      }
    },
    "ConfigurationAggregatorName" : {
      "description" : "The name of the aggregator.",
      "type" : "string",
      "pattern" : "[\\w\\-]+",
      "minLength" : 1,
      "maxLength" : 256
    },
    "ConfigurationAggregatorArn" : {
      "description" : "The Amazon Resource Name (ARN) of the aggregator.",
      "type" : "string"
    },
    "OrganizationAggregationSource" : {
      "$ref" : "#/definitions/OrganizationAggregationSource"
    },
    "Tags" : {
      "description" : "The tags for the configuration aggregator.",
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "AccountAggregationSource" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AllAwsRegions" : {
          "type" : "boolean"
        },
        "AwsRegions" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "AccountIds" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        }
      },
      "required" : [ "AccountIds" ]
    },
    "OrganizationAggregationSource" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AllAwsRegions" : {
          "type" : "boolean"
        },
        "AwsRegions" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "RoleArn" : {
          "type" : "string"
        }
      },
      "required" : [ "RoleArn" ]
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "readOnlyProperties" : [ "/properties/ConfigurationAggregatorArn" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "config:TagResource", "config:UntagResource", "config:ListTagsForResource" ]
  },
  "createOnlyProperties" : [ "/properties/ConfigurationAggregatorName" ],
  "primaryIdentifier" : [ "/properties/ConfigurationAggregatorName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "config:PutConfigurationAggregator", "config:DescribeConfigurationAggregators", "config:TagResource", "iam:PassRole", "organizations:EnableAWSServiceAccess", "organizations:ListDelegatedAdministrators" ]
    },
    "read" : {
      "permissions" : [ "config:DescribeConfigurationAggregators", "config:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "config:PutConfigurationAggregator", "config:DescribeConfigurationAggregators", "config:TagResource", "config:UntagResource", "config:ListTagsForResource", "iam:PassRole", "organizations:EnableAWSServiceAccess", "organizations:ListDelegatedAdministrators" ]
    },
    "delete" : {
      "permissions" : [ "config:DeleteConfigurationAggregator", "config:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "config:DescribeConfigurationAggregators" ]
    }
  }
}