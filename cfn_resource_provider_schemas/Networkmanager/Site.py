SCHEMA = {
  "typeName" : "AWS::NetworkManager::Site",
  "description" : "The AWS::NetworkManager::Site type describes a site.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-networkmanager.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a site resource.",
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
    "Location" : {
      "description" : "The location of the site",
      "type" : "object",
      "properties" : {
        "Address" : {
          "description" : "The physical address.",
          "type" : "string"
        },
        "Latitude" : {
          "description" : "The latitude.",
          "type" : "string"
        },
        "Longitude" : {
          "description" : "The longitude.",
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "SiteArn" : {
      "description" : "The Amazon Resource Name (ARN) of the site.",
      "type" : "string"
    },
    "SiteId" : {
      "description" : "The ID of the site.",
      "type" : "string"
    },
    "Description" : {
      "description" : "The description of the site.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "The tags for the site.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "GlobalNetworkId" : {
      "description" : "The ID of the global network.",
      "type" : "string"
    },
    "Location" : {
      "description" : "The location of the site.",
      "$ref" : "#/definitions/Location"
    },
    "CreatedAt" : {
      "description" : "The date and time that the device was created.",
      "type" : "string"
    },
    "State" : {
      "description" : "The state of the site.",
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
  "required" : [ "GlobalNetworkId" ],
  "readOnlyProperties" : [ "/properties/SiteId", "/properties/SiteArn", "/properties/State", "/properties/CreatedAt" ],
  "createOnlyProperties" : [ "/properties/GlobalNetworkId" ],
  "primaryIdentifier" : [ "/properties/GlobalNetworkId", "/properties/SiteId" ],
  "additionalIdentifiers" : [ [ "/properties/SiteArn" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "networkmanager:CreateSite", "networkmanager:GetSites", "networkmanager:TagResource" ]
    },
    "read" : {
      "permissions" : [ "networkmanager:GetSites" ]
    },
    "update" : {
      "permissions" : [ "networkmanager:GetSites", "networkmanager:ListTagsForResource", "networkmanager:TagResource", "networkmanager:UntagResource", "networkmanager:UpdateSite" ]
    },
    "delete" : {
      "permissions" : [ "networkmanager:GetSites", "networkmanager:DeleteSite" ]
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
      "permissions" : [ "networkmanager:GetSites" ]
    }
  }
}