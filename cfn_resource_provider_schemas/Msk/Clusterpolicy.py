SCHEMA = {
  "typeName" : "AWS::MSK::ClusterPolicy",
  "description" : "Resource Type definition for AWS::MSK::ClusterPolicy",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-msk",
  "definitions" : { },
  "properties" : {
    "Policy" : {
      "description" : "A policy document containing permissions to add to the specified cluster.",
      "type" : "object"
    },
    "ClusterArn" : {
      "description" : "The arn of the cluster for the resource policy.",
      "type" : "string",
      "pattern" : "^arn:[\\w-]+:kafka:[\\w-]+:\\d+:cluster.*\\Z"
    },
    "CurrentVersion" : {
      "description" : "The current version of the policy attached to the specified cluster",
      "type" : "string",
      "pattern" : "^(K)([a-zA-Z0-9]+)\\Z"
    }
  },
  "additionalProperties" : False,
  "required" : [ "Policy", "ClusterArn" ],
  "createOnlyProperties" : [ "/properties/ClusterArn" ],
  "readOnlyProperties" : [ "/properties/CurrentVersion" ],
  "primaryIdentifier" : [ "/properties/ClusterArn" ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "kafka:PutClusterPolicy", "kafka:GetClusterPolicy" ]
    },
    "read" : {
      "permissions" : [ "kafka:GetClusterPolicy" ]
    },
    "list" : {
      "permissions" : [ "kafka:GetClusterPolicy" ],
      "handlerSchema" : {
        "properties" : {
          "ClusterArn" : {
            "$ref" : "resource-schema.json#/properties/ClusterArn"
          }
        },
        "required" : [ "ClusterArn" ]
      }
    },
    "update" : {
      "permissions" : [ "kafka:PutClusterPolicy", "kafka:GetClusterPolicy" ]
    },
    "delete" : {
      "permissions" : [ "kafka:DeleteClusterPolicy", "kafka:GetClusterPolicy" ]
    }
  }
}