SCHEMA = {
  "typeName" : "AWS::OpsWorks::Instance",
  "description" : "Resource Type definition for AWS::OpsWorks::Instance",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "AvailabilityZone" : {
      "type" : "string"
    },
    "PrivateDnsName" : {
      "type" : "string"
    },
    "PrivateIp" : {
      "type" : "string"
    },
    "PublicDnsName" : {
      "type" : "string"
    },
    "PublicIp" : {
      "type" : "string"
    },
    "AgentVersion" : {
      "type" : "string"
    },
    "AmiId" : {
      "type" : "string"
    },
    "Architecture" : {
      "type" : "string"
    },
    "AutoScalingType" : {
      "type" : "string"
    },
    "BlockDeviceMappings" : {
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/BlockDeviceMapping"
      }
    },
    "EbsOptimized" : {
      "type" : "boolean"
    },
    "ElasticIps" : {
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "type" : "string"
      }
    },
    "Hostname" : {
      "type" : "string"
    },
    "InstallUpdatesOnBoot" : {
      "type" : "boolean"
    },
    "InstanceType" : {
      "type" : "string"
    },
    "LayerIds" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Os" : {
      "type" : "string"
    },
    "RootDeviceType" : {
      "type" : "string"
    },
    "SshKeyName" : {
      "type" : "string"
    },
    "StackId" : {
      "type" : "string"
    },
    "SubnetId" : {
      "type" : "string"
    },
    "Tenancy" : {
      "type" : "string"
    },
    "TimeBasedAutoScaling" : {
      "$ref" : "#/definitions/TimeBasedAutoScaling"
    },
    "VirtualizationType" : {
      "type" : "string"
    },
    "Volumes" : {
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "type" : "string"
      }
    }
  },
  "definitions" : {
    "BlockDeviceMapping" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DeviceName" : {
          "type" : "string"
        },
        "Ebs" : {
          "$ref" : "#/definitions/EbsBlockDevice"
        },
        "NoDevice" : {
          "type" : "string"
        },
        "VirtualName" : {
          "type" : "string"
        }
      }
    },
    "TimeBasedAutoScaling" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Friday" : {
          "type" : "object",
          "patternProperties" : {
            "[a-zA-Z0-9]+" : {
              "type" : "string"
            }
          }
        },
        "Monday" : {
          "type" : "object",
          "patternProperties" : {
            "[a-zA-Z0-9]+" : {
              "type" : "string"
            }
          }
        },
        "Saturday" : {
          "type" : "object",
          "patternProperties" : {
            "[a-zA-Z0-9]+" : {
              "type" : "string"
            }
          }
        },
        "Sunday" : {
          "type" : "object",
          "patternProperties" : {
            "[a-zA-Z0-9]+" : {
              "type" : "string"
            }
          }
        },
        "Thursday" : {
          "type" : "object",
          "patternProperties" : {
            "[a-zA-Z0-9]+" : {
              "type" : "string"
            }
          }
        },
        "Tuesday" : {
          "type" : "object",
          "patternProperties" : {
            "[a-zA-Z0-9]+" : {
              "type" : "string"
            }
          }
        },
        "Wednesday" : {
          "type" : "object",
          "patternProperties" : {
            "[a-zA-Z0-9]+" : {
              "type" : "string"
            }
          }
        }
      }
    },
    "EbsBlockDevice" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DeleteOnTermination" : {
          "type" : "boolean"
        },
        "Iops" : {
          "type" : "integer"
        },
        "SnapshotId" : {
          "type" : "string"
        },
        "VolumeSize" : {
          "type" : "integer"
        },
        "VolumeType" : {
          "type" : "string"
        }
      }
    }
  },
  "required" : [ "LayerIds", "InstanceType", "StackId" ],
  "readOnlyProperties" : [ "/properties/PublicDnsName", "/properties/PrivateDnsName", "/properties/PublicIp", "/properties/PrivateIp", "/properties/Id" ],
  "createOnlyProperties" : [ "/properties/Tenancy", "/properties/BlockDeviceMappings", "/properties/VirtualizationType", "/properties/TimeBasedAutoScaling", "/properties/RootDeviceType", "/properties/AutoScalingType", "/properties/StackId", "/properties/AvailabilityZone", "/properties/SubnetId", "/properties/EbsOptimized" ],
  "primaryIdentifier" : [ "/properties/Id" ]
}