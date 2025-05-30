SCHEMA = {
  "typeName" : "AWS::RoboMaker::SimulationApplication",
  "description" : "This schema is for testing purpose only.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Arn" : {
      "type" : "string",
      "pattern" : "arn:[\\w+=/,.@-]+:[\\w+=/,.@-]+:[\\w+=/,.@-]*:[0-9]*:[\\w+=,.@-]+(/[\\w+=,.@-]+)*"
    },
    "Tags" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "patternProperties" : {
        "^[a-zA-Z0-9-]{1,128}$" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 256
        }
      }
    },
    "RenderingEngine" : {
      "description" : "Information about a rendering engine.",
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "description" : "The name of the rendering engine.",
          "enum" : [ "OGRE" ]
        },
        "Version" : {
          "type" : "string",
          "description" : "The version of the rendering engine.",
          "pattern" : "1.x"
        }
      },
      "required" : [ "Name", "Version" ],
      "additionalProperties" : False
    },
    "RobotSoftwareSuite" : {
      "description" : "Information about a robot software suite.",
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "description" : "The name of the robot software suite.",
          "enum" : [ "ROS", "ROS2", "General" ]
        },
        "Version" : {
          "type" : "string",
          "description" : "The version of the robot software suite.",
          "enum" : [ "Kinetic", "Melodic", "Dashing", "Foxy" ]
        }
      },
      "required" : [ "Name" ],
      "additionalProperties" : False
    },
    "SourceConfig" : {
      "type" : "object",
      "description" : "Information about a source configuration.",
      "properties" : {
        "S3Bucket" : {
          "type" : "string",
          "description" : "The Amazon S3 bucket name.",
          "pattern" : "[a-z0-9][a-z0-9.\\-]*[a-z0-9]"
        },
        "S3Key" : {
          "type" : "string",
          "description" : "The s3 object key.",
          "minLength" : 1,
          "maxLength" : 1024
        },
        "Architecture" : {
          "type" : "string",
          "description" : "The target processor architecture for the application.",
          "enum" : [ "X86_64", "ARM64", "ARMHF" ]
        }
      },
      "required" : [ "S3Bucket", "S3Key", "Architecture" ],
      "additionalProperties" : False
    },
    "SimulationSoftwareSuite" : {
      "description" : "Information about a simulation software suite.",
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "description" : "The name of the simulation software suite.",
          "enum" : [ "Gazebo", "RosbagPlay", "SimulationRuntime" ]
        },
        "Version" : {
          "type" : "string",
          "description" : "The version of the simulation software suite.",
          "enum" : [ "7", "9", "11", "Kinetic", "Melodic", "Dashing", "Foxy" ]
        }
      },
      "required" : [ "Name" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "$ref" : "#/definitions/Arn"
    },
    "Name" : {
      "description" : "The name of the simulation application.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255,
      "pattern" : "[a-zA-Z0-9_\\-]*"
    },
    "CurrentRevisionId" : {
      "description" : "The current revision id.",
      "type" : "string"
    },
    "RenderingEngine" : {
      "description" : "The rendering engine for the simulation application.",
      "$ref" : "#/definitions/RenderingEngine"
    },
    "RobotSoftwareSuite" : {
      "description" : "The robot software suite used by the simulation application.",
      "$ref" : "#/definitions/RobotSoftwareSuite"
    },
    "SimulationSoftwareSuite" : {
      "description" : "The simulation software suite used by the simulation application.",
      "$ref" : "#/definitions/SimulationSoftwareSuite"
    },
    "Sources" : {
      "description" : "The sources of the simulation application.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/SourceConfig"
      }
    },
    "Environment" : {
      "description" : "The URI of the Docker image for the robot application.",
      "type" : "string"
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    }
  },
  "additionalProperties" : False,
  "required" : [ "RobotSoftwareSuite", "SimulationSoftwareSuite" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "writeOnlyProperties" : [ "/properties/RenderingEngine", "/properties/RobotSoftwareSuite/Version", "/properties/Sources", "/properties/SimulationSoftwareSuite/Version" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "robomaker:CreateSimulationApplication", "robomaker:TagResource", "robomaker:UntagResource", "ecr:BatchGetImage", "ecr:GetAuthorizationToken", "ecr:BatchCheckLayerAvailability", "ecr-public:GetAuthorizationToken", "sts:GetServiceBearerToken" ]
    },
    "read" : {
      "permissions" : [ "robomaker:DescribeSimulationApplication" ]
    },
    "update" : {
      "permissions" : [ "robomaker:TagResource", "robomaker:UntagResource", "robomaker:UpdateSimulationApplication", "ecr:BatchGetImage", "ecr:GetAuthorizationToken", "ecr:BatchCheckLayerAvailability", "ecr-public:GetAuthorizationToken" ]
    },
    "delete" : {
      "permissions" : [ "robomaker:DescribeSimulationApplication", "robomaker:DeleteSimulationApplication" ]
    },
    "list" : {
      "permissions" : [ "robomaker:ListSimulationApplications" ]
    }
  }
}