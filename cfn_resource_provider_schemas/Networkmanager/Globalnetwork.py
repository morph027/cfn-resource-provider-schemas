SCHEMA = {
  "typeName" : "AWS::NetworkManager::GlobalNetwork",
  "description" : "The AWS::NetworkManager::GlobalNetwork type specifies a global network of the user's account",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-networkmanager.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a global network resource.",
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
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the global network.",
      "type" : "string"
    },
    "Id" : {
      "description" : "The ID of the global network.",
      "type" : "string"
    },
    "Description" : {
      "description" : "The description of the global network.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "The tags for the global network.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "CreatedAt" : {
      "description" : "The date and time that the global network was created.",
      "type" : "string"
    },
    "State" : {
      "description" : "The state of the global network.",
      "type" : "string"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "networkmanager:TagResource", "networkmanager:UntagResource", "networkmanager:ListTagsForResource" ]
  },
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "additionalIdentifiers" : [ [ "/properties/Arn" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "networkmanager:CreateGlobalNetwork", "networkmanager:DescribeGlobalNetworks", "networkmanager:TagResource", "iam:CreateServiceLinkedRole" ]
    },
    "read" : {
      "permissions" : [ "networkmanager:DescribeGlobalNetworks" ]
    },
    "update" : {
      "permissions" : [ "networkmanager:UpdateGlobalNetwork", "networkmanager:DescribeGlobalNetworks", "networkmanager:TagResource", "networkmanager:UntagResource", "networkmanager:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "networkmanager:DeleteGlobalNetwork", "networkmanager:DescribeGlobalNetworks" ]
    },
    "list" : {
      "permissions" : [ "networkmanager:DescribeGlobalNetworks" ]
    }
  }
}