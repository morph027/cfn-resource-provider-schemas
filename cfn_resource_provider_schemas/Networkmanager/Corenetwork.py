SCHEMA = {
  "typeName" : "AWS::NetworkManager::CoreNetwork",
  "description" : "AWS::NetworkManager::CoreNetwork Resource Type Definition.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-networkmanager/aws-networkmanager-corenetwork",
  "properties" : {
    "GlobalNetworkId" : {
      "description" : "The ID of the global network that your core network is a part of.",
      "type" : "string"
    },
    "CoreNetworkId" : {
      "description" : "The Id of core network",
      "type" : "string"
    },
    "CoreNetworkArn" : {
      "description" : "The ARN (Amazon resource name) of core network",
      "type" : "string"
    },
    "PolicyDocument" : {
      "description" : "Live policy document for the core network, you must provide PolicyDocument in Json Format",
      "type" : "object"
    },
    "Description" : {
      "description" : "The description of core network",
      "type" : "string"
    },
    "CreatedAt" : {
      "description" : "The creation time of core network",
      "type" : "string"
    },
    "State" : {
      "description" : "The state of core network",
      "type" : "string"
    },
    "Segments" : {
      "description" : "The segments within a core network.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/CoreNetworkSegment"
      }
    },
    "NetworkFunctionGroups" : {
      "description" : "The network function groups within a core network.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/CoreNetworkNetworkFunctionGroup"
      }
    },
    "Edges" : {
      "description" : "The edges within a core network.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/CoreNetworkEdge"
      }
    },
    "OwnerAccount" : {
      "description" : "Owner of the core network",
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
    }
  },
  "definitions" : {
    "CoreNetworkSegment" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "description" : "Name of segment"
        },
        "EdgeLocations" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "type" : "string",
            "description" : "The Regions where the edges are located."
          }
        },
        "SharedSegments" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "type" : "string",
            "description" : "The shared segments of a core network."
          }
        }
      },
      "additionalProperties" : False
    },
    "CoreNetworkNetworkFunctionGroup" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "description" : "Name of network function group"
        },
        "EdgeLocations" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "type" : "string",
            "description" : "The Regions where the edges are located."
          }
        },
        "Segments" : {
          "type" : "object",
          "properties" : {
            "SendTo" : {
              "type" : "array",
              "insertionOrder" : False,
              "items" : {
                "type" : "string",
                "description" : "The send-to segments."
              }
            },
            "SendVia" : {
              "type" : "array",
              "insertionOrder" : False,
              "items" : {
                "type" : "string",
                "description" : "The send-via segments."
              }
            }
          },
          "additionalProperties" : False
        }
      },
      "additionalProperties" : False
    },
    "CoreNetworkEdge" : {
      "type" : "object",
      "properties" : {
        "EdgeLocation" : {
          "type" : "string",
          "description" : "The Region where a core network edge is located."
        },
        "Asn" : {
          "type" : "number",
          "description" : "The ASN of a core network edge."
        },
        "InsideCidrBlocks" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "type" : "string",
            "description" : "The inside IP addresses used for core network edges."
          }
        }
      },
      "additionalProperties" : False
    },
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
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
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
  "readOnlyProperties" : [ "/properties/OwnerAccount", "/properties/CoreNetworkId", "/properties/CoreNetworkArn", "/properties/CreatedAt", "/properties/State", "/properties/Segments", "/properties/NetworkFunctionGroups", "/properties/Edges" ],
  "createOnlyProperties" : [ "/properties/GlobalNetworkId" ],
  "primaryIdentifier" : [ "/properties/CoreNetworkId" ],
  "additionalIdentifiers" : [ [ "/properties/CoreNetworkArn" ], [ "/properties/GlobalNetworkId" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "networkmanager:CreateCoreNetwork", "networkmanager:GetCoreNetwork", "networkmanager:GetCoreNetworkPolicy", "networkmanager:TagResource", "ec2:DescribeRegions" ],
      "timeoutInMinutes" : 720
    },
    "read" : {
      "permissions" : [ "networkmanager:GetCoreNetwork", "networkmanager:GetCoreNetworkPolicy" ]
    },
    "update" : {
      "permissions" : [ "networkmanager:UpdateCoreNetwork", "networkmanager:GetCoreNetwork", "networkmanager:ListTagsForResource", "networkmanager:PutCoreNetworkPolicy", "networkmanager:GetCoreNetworkPolicy", "networkmanager:ExecuteCoreNetworkChangeSet", "networkmanager:TagResource", "networkmanager:UntagResource", "ec2:DescribeRegions" ],
      "timeoutInMinutes" : 720
    },
    "delete" : {
      "permissions" : [ "networkmanager:DeleteCoreNetwork", "networkmanager:UntagResource", "networkmanager:GetCoreNetwork", "networkmanager:GetCoreNetworkPolicy", "ec2:DescribeRegions" ],
      "timeoutInMinutes" : 720
    },
    "list" : {
      "permissions" : [ "networkmanager:ListCoreNetworks" ]
    }
  }
}