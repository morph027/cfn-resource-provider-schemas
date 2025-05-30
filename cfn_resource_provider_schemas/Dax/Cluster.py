SCHEMA = {
  "typeName" : "AWS::DAX::Cluster",
  "description" : "Resource Type definition for AWS::DAX::Cluster",
  "additionalProperties" : False,
  "properties" : {
    "SSESpecification" : {
      "$ref" : "#/definitions/SSESpecification"
    },
    "ClusterDiscoveryEndpointURL" : {
      "type" : "string"
    },
    "Description" : {
      "type" : "string"
    },
    "ReplicationFactor" : {
      "type" : "integer"
    },
    "ParameterGroupName" : {
      "type" : "string"
    },
    "AvailabilityZones" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "type" : "string"
      }
    },
    "IAMRoleARN" : {
      "type" : "string"
    },
    "SubnetGroupName" : {
      "type" : "string"
    },
    "PreferredMaintenanceWindow" : {
      "type" : "string"
    },
    "ClusterEndpointEncryptionType" : {
      "type" : "string"
    },
    "NotificationTopicARN" : {
      "type" : "string"
    },
    "SecurityGroupIds" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "type" : "string"
      }
    },
    "NodeType" : {
      "type" : "string"
    },
    "ClusterName" : {
      "type" : "string"
    },
    "ClusterDiscoveryEndpoint" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "Arn" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "object"
    }
  },
  "definitions" : {
    "SSESpecification" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SSEEnabled" : {
          "type" : "boolean"
        }
      }
    }
  },
  "required" : [ "ReplicationFactor", "IAMRoleARN", "NodeType" ],
  "createOnlyProperties" : [ "/properties/IAMRoleARN", "/properties/SSESpecification", "/properties/ClusterEndpointEncryptionType", "/properties/ClusterName", "/properties/NodeType", "/properties/SubnetGroupName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/ClusterDiscoveryEndpoint", "/properties/Arn", "/properties/ClusterDiscoveryEndpointURL" ]
}