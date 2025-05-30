SCHEMA = {
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "tagging" : {
    "tagOnCreate" : False,
    "taggable" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "read" : {
      "permissions" : [ "ecs:DescribeClusters" ]
    },
    "create" : {
      "permissions" : [ "ecs:DescribeClusters", "ecs:PutClusterCapacityProviders", "ecs:DescribeCapacityProviders" ]
    },
    "update" : {
      "permissions" : [ "ecs:DescribeClusters", "ecs:PutClusterCapacityProviders" ]
    },
    "list" : {
      "permissions" : [ "ecs:DescribeClusters", "ecs:ListClusters" ]
    },
    "delete" : {
      "permissions" : [ "ecs:PutClusterCapacityProviders", "ecs:DescribeClusters" ]
    }
  },
  "typeName" : "AWS::ECS::ClusterCapacityProviderAssociations",
  "description" : "Associate a set of ECS Capacity Providers with a specified ECS Cluster",
  "createOnlyProperties" : [ "/properties/Cluster" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/Cluster" ],
  "definitions" : {
    "DefaultCapacityProviderStrategy" : {
      "description" : "List of capacity providers to associate with the cluster",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/CapacityProviderStrategy"
      }
    },
    "CapacityProvider" : {
      "description" : "If using ec2 auto-scaling, the name of the associated capacity provider. Otherwise FARGATE, FARGATE_SPOT.",
      "anyOf" : [ {
        "type" : "string",
        "enum" : [ "FARGATE", "FARGATE_SPOT" ]
      }, {
        "minLength" : 1,
        "type" : "string",
        "maxLength" : 2048
      } ],
      "type" : "string"
    },
    "CapacityProviders" : {
      "uniqueItems" : True,
      "description" : "List of capacity providers to associate with the cluster",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/CapacityProvider"
      }
    },
    "Cluster" : {
      "minLength" : 1,
      "description" : "The name of the cluster",
      "type" : "string",
      "maxLength" : 2048
    },
    "CapacityProviderStrategy" : {
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "CapacityProvider" : {
          "$ref" : "#/definitions/CapacityProvider"
        },
        "Base" : {
          "maximum" : 100000,
          "type" : "integer",
          "minimum" : 0
        },
        "Weight" : {
          "maximum" : 1000,
          "type" : "integer",
          "minimum" : 0
        }
      },
      "required" : [ "CapacityProvider" ]
    }
  },
  "properties" : {
    "DefaultCapacityProviderStrategy" : {
      "$ref" : "#/definitions/DefaultCapacityProviderStrategy"
    },
    "CapacityProviders" : {
      "$ref" : "#/definitions/CapacityProviders"
    },
    "Cluster" : {
      "$ref" : "#/definitions/Cluster"
    }
  },
  "required" : [ "CapacityProviders", "Cluster", "DefaultCapacityProviderStrategy" ]
}