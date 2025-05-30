SCHEMA = {
  "typeName" : "AWS::NeptuneGraph::Graph",
  "description" : "The AWS::NeptuneGraph::Graph resource creates an Amazon NeptuneGraph Graph.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-neptunegraph",
  "properties" : {
    "DeletionProtection" : {
      "description" : "Value that indicates whether the Graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.\n\n_Default_: If not specified, the default value is True.",
      "type" : "boolean"
    },
    "GraphName" : {
      "description" : "Contains a user-supplied name for the Graph. \n\nIf you don't specify a name, we generate a unique Graph Name using a combination of Stack Name and a UUID comprising of 4 characters.\n\n_Important_: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.",
      "type" : "string",
      "pattern" : "^[a-zA-z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*$",
      "minLength" : 1,
      "maxLength" : 63
    },
    "ProvisionedMemory" : {
      "description" : "Memory for the Graph.",
      "type" : "integer"
    },
    "PublicConnectivity" : {
      "description" : "Specifies whether the Graph can be reached over the internet. Access to all graphs requires IAM authentication.\n\nWhen the Graph is publicly reachable, its Domain Name System (DNS) endpoint resolves to the public IP address from the internet.\n\nWhen the Graph isn't publicly reachable, you need to create a PrivateGraphEndpoint in a given VPC to ensure the DNS name resolves to a private IP address that is reachable from the VPC.\n\n_Default_: If not specified, the default value is False.",
      "type" : "boolean"
    },
    "ReplicaCount" : {
      "description" : "Specifies the number of replicas you want when finished. All replicas will be provisioned in different availability zones.\n\nReplica Count should always be less than or equal to 2.\n\n_Default_: If not specified, the default value is 1.",
      "type" : "integer"
    },
    "Tags" : {
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "description" : "The tags associated with this graph.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "VectorSearchConfiguration" : {
      "description" : "Vector Search Configuration",
      "$ref" : "#/definitions/VectorSearchConfiguration"
    },
    "Endpoint" : {
      "description" : "The connection endpoint for the graph. For example: `g-12a3bcdef4.us-east-1.neptune-graph.amazonaws.com`",
      "type" : "string"
    },
    "GraphArn" : {
      "description" : "Graph resource ARN",
      "type" : "string"
    },
    "GraphId" : {
      "description" : "The auto-generated id assigned by the service.",
      "type" : "string"
    }
  },
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key" ]
    },
    "VectorSearchConfiguration" : {
      "description" : "The vector search configuration.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "VectorSearchDimension" : {
          "type" : "integer",
          "description" : "The vector search dimension"
        }
      },
      "required" : [ "VectorSearchDimension" ]
    }
  },
  "additionalProperties" : False,
  "required" : [ "ProvisionedMemory" ],
  "propertyTransform" : {
    "/properties/GraphId" : "$lowercase(GraphId)",
    "/properties/GraphName" : "$lowercase(GraphName)"
  },
  "readOnlyProperties" : [ "/properties/GraphArn", "/properties/GraphId", "/properties/Endpoint" ],
  "createOnlyProperties" : [ "/properties/GraphName", "/properties/ReplicaCount", "/properties/VectorSearchConfiguration" ],
  "conditionalCreateOnlyProperties" : [ "/properties/ProvisionedMemory" ],
  "primaryIdentifier" : [ "/properties/GraphId" ],
  "additionalIdentifiers" : [ [ "/properties/GraphName" ] ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:PassRole", "neptune-graph:CreateGraph", "neptune-graph:GetGraph", "neptune-graph:ListTagsForResource", "neptune-graph:TagResource", "kms:DescribeKey", "kms:CreateGrant", "kms:Decrypt", "iam:CreateServiceLinkedRole" ],
      "timeoutInMinutes" : 2160
    },
    "read" : {
      "permissions" : [ "neptune-graph:GetGraph", "neptune-graph:ListTagsForResource", "kms:DescribeKey", "kms:CreateGrant", "kms:Decrypt" ],
      "timeoutInMinutes" : 2160
    },
    "update" : {
      "permissions" : [ "iam:PassRole", "neptune-graph:GetGraph", "neptune-graph:ListTagsForResource", "neptune-graph:TagResource", "neptune-graph:UntagResource", "neptune-graph:UpdateGraph", "kms:DescribeKey", "kms:CreateGrant", "kms:Decrypt" ],
      "timeoutInMinutes" : 2160
    },
    "delete" : {
      "permissions" : [ "neptune-graph:DeleteGraph", "neptune-graph:GetGraph", "kms:DescribeKey", "kms:CreateGrant", "kms:Decrypt" ],
      "timeoutInMinutes" : 2160
    },
    "list" : {
      "permissions" : [ "neptune-graph:GetGraph", "neptune-graph:ListGraphs", "kms:DescribeKey", "kms:CreateGrant", "kms:Decrypt" ],
      "timeoutInMinutes" : 2160
    }
  }
}