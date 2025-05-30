SCHEMA = {
  "typeName" : "AWS::NetworkManager::Link",
  "description" : "The AWS::NetworkManager::Link type describes a link.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-networkmanager.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a link resource.",
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
    },
    "Bandwidth" : {
      "description" : "The bandwidth for the link.",
      "type" : "object",
      "properties" : {
        "DownloadSpeed" : {
          "description" : "Download speed in Mbps.",
          "type" : "integer"
        },
        "UploadSpeed" : {
          "description" : "Upload speed in Mbps.",
          "type" : "integer"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "LinkArn" : {
      "description" : "The Amazon Resource Name (ARN) of the link.",
      "type" : "string"
    },
    "LinkId" : {
      "description" : "The ID of the link.",
      "type" : "string"
    },
    "GlobalNetworkId" : {
      "description" : "The ID of the global network.",
      "type" : "string"
    },
    "SiteId" : {
      "description" : "The ID of the site",
      "type" : "string"
    },
    "Bandwidth" : {
      "description" : "The Bandwidth for the link.",
      "$ref" : "#/definitions/Bandwidth"
    },
    "Provider" : {
      "description" : "The provider of the link.",
      "type" : "string"
    },
    "Description" : {
      "description" : "The description of the link.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "The tags for the link.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Type" : {
      "description" : "The type of the link.",
      "type" : "string"
    },
    "CreatedAt" : {
      "description" : "The date and time that the device was created.",
      "type" : "string"
    },
    "State" : {
      "description" : "The state of the link.",
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
  "required" : [ "GlobalNetworkId", "SiteId", "Bandwidth" ],
  "readOnlyProperties" : [ "/properties/LinkId", "/properties/LinkArn", "/properties/CreatedAt", "/properties/State" ],
  "createOnlyProperties" : [ "/properties/GlobalNetworkId", "/properties/SiteId" ],
  "primaryIdentifier" : [ "/properties/GlobalNetworkId", "/properties/LinkId" ],
  "additionalIdentifiers" : [ [ "/properties/LinkArn" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "networkmanager:CreateLink", "networkmanager:GetLinks", "networkmanager:TagResource" ]
    },
    "read" : {
      "permissions" : [ "networkmanager:GetLinks" ]
    },
    "update" : {
      "permissions" : [ "networkmanager:ListTagsForResource", "networkmanager:TagResource", "networkmanager:GetLinks", "networkmanager:UntagResource", "networkmanager:UpdateLink" ]
    },
    "delete" : {
      "permissions" : [ "networkmanager:GetLinks", "networkmanager:DeleteLink" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "GlobalNetworkId" : {
            "$ref" : "resource-schema.json#/properties/GlobalNetworkId"
          }
        },
        "required" : [ "GlobalNetworkId" ]
      },
      "permissions" : [ "networkmanager:GetLinks" ]
    }
  }
}