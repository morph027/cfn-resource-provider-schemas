SCHEMA = {
  "typeName" : "AWS::MediaLive::Cluster",
  "description" : "Definition of AWS::MediaLive::Cluster Resource Type",
  "definitions" : {
    "ClusterNetworkSettings" : {
      "type" : "object",
      "description" : "On premises settings which will have the interface network mappings and default Output logical interface",
      "properties" : {
        "DefaultRoute" : {
          "type" : "string",
          "description" : "Default value if the customer does not define it in channel Output API"
        },
        "InterfaceMappings" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/InterfaceMapping"
          },
          "description" : "Network mappings for the cluster"
        }
      },
      "additionalProperties" : False
    },
    "ClusterState" : {
      "type" : "string",
      "description" : "The current state of the Cluster.",
      "enum" : [ "CREATING", "CREATE_FAILED", "ACTIVE", "DELETING", "DELETED" ]
    },
    "ClusterType" : {
      "type" : "string",
      "description" : "The hardware type for the cluster.",
      "enum" : [ "ON_PREMISES", "OUTPOSTS_RACK", "OUTPOSTS_SERVER", "EC2" ]
    },
    "InterfaceMapping" : {
      "type" : "object",
      "description" : "Network mappings for the cluster",
      "properties" : {
        "LogicalInterfaceName" : {
          "type" : "string",
          "description" : "logical interface name, unique in the list"
        },
        "NetworkId" : {
          "type" : "string",
          "description" : "Network Id to be associated with the logical interface name, can be duplicated in list"
        }
      },
      "additionalProperties" : False
    },
    "InterfaceNetworkMapping" : {
      "type" : "object",
      "description" : "Network mappings for the cluster",
      "properties" : {
        "LogicalInterfaceName" : {
          "type" : "string",
          "description" : "logical interface name, unique in the list"
        },
        "NetworkId" : {
          "type" : "string",
          "description" : "Network Id to be associated with the logical interface name, can be duplicated in list"
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
  "properties" : {
    "Arn" : {
      "type" : "string",
      "pattern" : "^arn:.+:medialive:.+:cluster:.+$",
      "description" : "The ARN of the Cluster."
    },
    "ChannelIds" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "description" : "MediaLive Channel Ids"
      },
      "description" : "The MediaLive Channels that are currently running on Nodes in this Cluster."
    },
    "ClusterType" : {
      "$ref" : "#/definitions/ClusterType"
    },
    "Id" : {
      "type" : "string",
      "description" : "The unique ID of the Cluster."
    },
    "InstanceRoleArn" : {
      "type" : "string",
      "pattern" : "^arn:.+:iam:.+:role/.+$",
      "description" : "The IAM role your nodes will use."
    },
    "Name" : {
      "type" : "string",
      "description" : "The user-specified name of the Cluster to be created."
    },
    "NetworkSettings" : {
      "$ref" : "#/definitions/ClusterNetworkSettings"
    },
    "State" : {
      "$ref" : "#/definitions/ClusterState"
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
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "medialive:CreateTags", "medialive:DeleteTags" ]
  },
  "readOnlyProperties" : [ "/properties/Arn", "/properties/ChannelIds", "/properties/Id", "/properties/State" ],
  "createOnlyProperties" : [ "/properties/ClusterType", "/properties/InstanceRoleArn" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "medialive:CreateCluster", "medialive:DescribeCluster", "medialive:CreateTags", "ecs:CreateCluster", "ecs:RegisterTaskDefinition", "ecs:TagResource", "ecs:CreateService", "iam:PassRole", "medialive:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "medialive:DescribeCluster", "medialive:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "medialive:UpdateCluster", "medialive:DescribeCluster", "medialive:CreateTags", "medialive:DeleteTags", "medialive:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "medialive:DeleteCluster", "medialive:DescribeCluster", "ecs:DeleteService" ]
    },
    "list" : {
      "permissions" : [ "medialive:ListClusters" ]
    }
  },
  "additionalProperties" : False
}