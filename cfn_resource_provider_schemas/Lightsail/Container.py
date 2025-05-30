SCHEMA = {
  "typeName" : "AWS::Lightsail::Container",
  "description" : "Resource Type definition for AWS::Lightsail::Container",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-lightsail.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key" ],
      "additionalProperties" : False
    },
    "HealthCheckConfig" : {
      "description" : "Describes the health check configuration of an Amazon Lightsail container service.",
      "type" : "object",
      "properties" : {
        "HealthyThreshold" : {
          "type" : "integer",
          "description" : "The number of consecutive health checks successes required before moving the container to the Healthy state. The default value is 2."
        },
        "IntervalSeconds" : {
          "type" : "integer",
          "description" : "The approximate interval, in seconds, between health checks of an individual container. You can specify between 5 and 300 seconds. The default value is 5."
        },
        "Path" : {
          "type" : "string",
          "description" : "The path on the container on which to perform the health check. The default value is /."
        },
        "SuccessCodes" : {
          "type" : "string",
          "description" : "The HTTP codes to use when checking for a successful response from a container. You can specify values between 200 and 499. You can specify multiple values (for example, 200,202) or a range of values (for example, 200-299)."
        },
        "TimeoutSeconds" : {
          "type" : "integer",
          "description" : "The amount of time, in seconds, during which no response means a failed health check. You can specify between 2 and 60 seconds. The default value is 2."
        },
        "UnhealthyThreshold" : {
          "type" : "integer",
          "description" : "The number of consecutive health check failures required before moving the container to the Unhealthy state. The default value is 2."
        }
      },
      "additionalProperties" : False
    },
    "PublicEndpoint" : {
      "description" : "Describes the settings of a public endpoint for an Amazon Lightsail container service.",
      "type" : "object",
      "properties" : {
        "ContainerName" : {
          "type" : "string",
          "description" : "The name of the container for the endpoint."
        },
        "ContainerPort" : {
          "type" : "integer",
          "description" : "The port of the container to which traffic is forwarded to."
        },
        "HealthCheckConfig" : {
          "$ref" : "#/definitions/HealthCheckConfig",
          "description" : "An object that describes the health check configuration of the container."
        }
      },
      "additionalProperties" : False
    },
    "EnvironmentVariable" : {
      "type" : "object",
      "properties" : {
        "Variable" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "PortInfo" : {
      "type" : "object",
      "properties" : {
        "Port" : {
          "type" : "string"
        },
        "Protocol" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "Container" : {
      "description" : "Describes the settings of a container that will be launched, or that is launched, to an Amazon Lightsail container service.",
      "type" : "object",
      "properties" : {
        "ContainerName" : {
          "type" : "string",
          "description" : "The name of the container."
        },
        "Command" : {
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "items" : {
            "type" : "string"
          },
          "description" : "The launch command for the container."
        },
        "Environment" : {
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/EnvironmentVariable"
          },
          "description" : "The environment variables of the container."
        },
        "Image" : {
          "type" : "string",
          "description" : "The name of the image used for the container."
        },
        "Ports" : {
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/PortInfo"
          },
          "description" : "The open firewall ports of the container."
        }
      },
      "additionalProperties" : False
    },
    "ContainerServiceDeployment" : {
      "description" : "Describes a container deployment configuration of an Amazon Lightsail container service.",
      "type" : "object",
      "properties" : {
        "Containers" : {
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/Container"
          },
          "description" : "An object that describes the configuration for the containers of the deployment."
        },
        "PublicEndpoint" : {
          "$ref" : "#/definitions/PublicEndpoint",
          "description" : "An object that describes the endpoint of the deployment."
        }
      },
      "additionalProperties" : False
    },
    "PublicDomainName" : {
      "description" : "The public domain name to use with the container service, such as example.com and www.example.com.",
      "type" : "object",
      "properties" : {
        "CertificateName" : {
          "type" : "string"
        },
        "DomainNames" : {
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "items" : {
            "type" : "string"
          },
          "description" : "An object that describes the configuration for the containers of the deployment."
        }
      },
      "additionalProperties" : False
    },
    "PrivateRegistryAccess" : {
      "description" : "An object to describe the configuration for the container service to access private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.",
      "type" : "object",
      "properties" : {
        "EcrImagePullerRole" : {
          "description" : "An object to describe a request to activate or deactivate the role that you can use to grant an Amazon Lightsail container service access to Amazon Elastic Container Registry (Amazon ECR) private repositories.",
          "type" : "object",
          "properties" : {
            "IsActive" : {
              "type" : "boolean",
              "description" : "A Boolean value that indicates whether to activate the role."
            },
            "PrincipalArn" : {
              "type" : "string",
              "description" : "The Amazon Resource Name (ARN) of the role, if it is activated."
            }
          },
          "additionalProperties" : False
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ServiceName" : {
      "description" : "The name for the container service.",
      "type" : "string",
      "pattern" : "^[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]+[a-z0-9]$",
      "minLength" : 1,
      "maxLength" : 63
    },
    "Power" : {
      "description" : "The power specification for the container service.",
      "type" : "string"
    },
    "ContainerArn" : {
      "type" : "string"
    },
    "Scale" : {
      "description" : "The scale specification for the container service.",
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 20
    },
    "PublicDomainNames" : {
      "description" : "The public domain names to use with the container service, such as example.com and www.example.com.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/PublicDomainName"
      }
    },
    "ContainerServiceDeployment" : {
      "$ref" : "#/definitions/ContainerServiceDeployment",
      "description" : "Describes a container deployment configuration of an Amazon Lightsail container service."
    },
    "IsDisabled" : {
      "description" : "A Boolean value to indicate whether the container service is disabled.",
      "type" : "boolean"
    },
    "PrivateRegistryAccess" : {
      "$ref" : "#/definitions/PrivateRegistryAccess",
      "description" : "A Boolean value to indicate whether the container service has access to private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories."
    },
    "Url" : {
      "description" : "The publicly accessible URL of the container service.",
      "type" : "string"
    },
    "PrincipalArn" : {
      "description" : "The principal ARN of the container service.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "ServiceName", "Power", "Scale" ],
  "readOnlyProperties" : [ "/properties/ContainerArn", "/properties/Url", "/properties/PrincipalArn", "/properties/PrivateRegistryAccess/EcrImagePullerRole/PrincipalArn" ],
  "primaryIdentifier" : [ "/properties/ServiceName" ],
  "createOnlyProperties" : [ "/properties/ServiceName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "lightsail:CreateContainerService", "lightsail:CreateContainerServiceDeployment", "lightsail:GetContainerServices", "lightsail:TagResource", "lightsail:UntagResource", "lightsail:UpdateContainerService" ]
    },
    "read" : {
      "permissions" : [ "lightsail:GetContainerServices" ]
    },
    "delete" : {
      "permissions" : [ "lightsail:DeleteContainerService", "lightsail:GetContainerServices" ]
    },
    "list" : {
      "permissions" : [ "lightsail:GetContainerServices" ]
    },
    "update" : {
      "permissions" : [ "lightsail:CreateContainerServiceDeployment", "lightsail:GetContainerServices", "lightsail:TagResource", "lightsail:UntagResource", "lightsail:UpdateContainerService" ],
      "timeoutInMinutes" : 2160
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "lightsail:TagResource", "lightsail:UntagResource" ]
  }
}