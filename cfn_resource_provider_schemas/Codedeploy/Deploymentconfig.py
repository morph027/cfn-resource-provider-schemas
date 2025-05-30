SCHEMA = {
  "typeName" : "AWS::CodeDeploy::DeploymentConfig",
  "description" : "Resource Type definition for AWS::CodeDeploy::DeploymentConfig",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-codedeploy",
  "definitions" : {
    "TimeBasedLinear" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "LinearInterval" : {
          "type" : "integer"
        },
        "LinearPercentage" : {
          "type" : "integer"
        }
      },
      "required" : [ "LinearInterval", "LinearPercentage" ]
    },
    "TimeBasedCanary" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CanaryPercentage" : {
          "type" : "integer"
        },
        "CanaryInterval" : {
          "type" : "integer"
        }
      },
      "required" : [ "CanaryPercentage", "CanaryInterval" ]
    },
    "TrafficRoutingConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Type" : {
          "type" : "string"
        },
        "TimeBasedLinear" : {
          "$ref" : "#/definitions/TimeBasedLinear"
        },
        "TimeBasedCanary" : {
          "$ref" : "#/definitions/TimeBasedCanary"
        }
      },
      "required" : [ "Type" ]
    },
    "MinimumHealthyHostsPerZone" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "integer"
        },
        "Type" : {
          "type" : "string"
        }
      },
      "required" : [ "Type", "Value" ]
    },
    "ZonalConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FirstZoneMonitorDurationInSeconds" : {
          "type" : "integer",
          "format" : "int64"
        },
        "MonitorDurationInSeconds" : {
          "type" : "integer",
          "format" : "int64"
        },
        "MinimumHealthyHostsPerZone" : {
          "$ref" : "#/definitions/MinimumHealthyHostsPerZone"
        }
      },
      "required" : [ ]
    },
    "MinimumHealthyHosts" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "integer"
        },
        "Type" : {
          "type" : "string"
        }
      },
      "required" : [ "Type", "Value" ]
    }
  },
  "properties" : {
    "ComputePlatform" : {
      "description" : "The destination platform type for the deployment (Lambda, Server, or ECS).",
      "type" : "string"
    },
    "DeploymentConfigName" : {
      "description" : "A name for the deployment configuration. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment configuration name. For more information, see Name Type.",
      "type" : "string"
    },
    "MinimumHealthyHosts" : {
      "description" : "The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value.",
      "$ref" : "#/definitions/MinimumHealthyHosts"
    },
    "ZonalConfig" : {
      "description" : "The zonal deployment config that specifies how the zonal deployment behaves",
      "$ref" : "#/definitions/ZonalConfig"
    },
    "TrafficRoutingConfig" : {
      "description" : "The configuration that specifies how the deployment traffic is routed.",
      "$ref" : "#/definitions/TrafficRoutingConfig"
    }
  },
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/DeploymentConfigName", "/properties/MinimumHealthyHosts", "/properties/ComputePlatform", "/properties/ZonalConfig", "/properties/TrafficRoutingConfig" ],
  "primaryIdentifier" : [ "/properties/DeploymentConfigName" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "codedeploy:CreateDeploymentConfig" ]
    },
    "read" : {
      "permissions" : [ "codedeploy:GetDeploymentConfig" ]
    },
    "delete" : {
      "permissions" : [ "codedeploy:GetDeploymentConfig", "codedeploy:DeleteDeploymentConfig" ]
    },
    "list" : {
      "permissions" : [ "codedeploy:ListDeploymentConfigs" ]
    }
  }
}