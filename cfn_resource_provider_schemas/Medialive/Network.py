SCHEMA = {
  "typeName" : "AWS::MediaLive::Network",
  "description" : "Resource schema for AWS::MediaLive::Network.",
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : "The ARN of the Network."
    },
    "AssociatedClusterIds" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "description" : "Cluster Ids which have this network ID in their Interface Network Mappings"
      }
    },
    "Id" : {
      "type" : "string",
      "description" : "The unique ID of the Network."
    },
    "IpPools" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/IpPool"
      },
      "description" : "The list of IP address cidr pools for the network"
    },
    "Name" : {
      "type" : "string",
      "description" : "The user-specified name of the Network to be created."
    },
    "Routes" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Route"
      },
      "description" : "The routes for the network"
    },
    "State" : {
      "$ref" : "#/definitions/NetworkState",
      "description" : "The current state of the Network."
    },
    "Tags" : {
      "description" : "A collection of key-value pairs.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tags"
      }
    }
  },
  "definitions" : {
    "IpPool" : {
      "type" : "object",
      "description" : "IP address cidr pool",
      "properties" : {
        "Cidr" : {
          "type" : "string",
          "description" : "IP address cidr pool"
        }
      },
      "additionalProperties" : False
    },
    "NetworkState" : {
      "type" : "string",
      "enum" : [ "CREATING", "CREATE_FAILED", "ACTIVE", "DELETING", "IDLE", "IN_USE", "UPDATING", "DELETED", "DELETE_FAILED" ]
    },
    "Route" : {
      "type" : "object",
      "properties" : {
        "Cidr" : {
          "type" : "string",
          "description" : "Ip address cidr"
        },
        "Gateway" : {
          "type" : "string",
          "description" : "IP address for the route packet paths"
        }
      },
      "additionalProperties" : False
    },
    "Tags" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "required" : [ "Name", "IpPools" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id", "/properties/State", "/properties/AssociatedClusterIds" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "medialive:CreateTags", "medialive:DeleteTags" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "medialive:CreateNetwork", "medialive:CreateTags", "medialive:DescribeNetwork", "medialive:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "medialive:DescribeNetwork", "medialive:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "medialive:UpdateNetwork", "medialive:CreateTags", "medialive:DeleteTags", "medialive:DescribeNetwork", "medialive:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "medialive:DeleteNetwork", "medialive:DescribeNetwork" ]
    },
    "list" : {
      "permissions" : [ "medialive:ListNetworks" ]
    }
  },
  "additionalProperties" : False
}