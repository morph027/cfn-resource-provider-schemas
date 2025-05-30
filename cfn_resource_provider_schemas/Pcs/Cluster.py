SCHEMA = {
  "typeName" : "AWS::PCS::Cluster",
  "description" : "AWS::PCS::Cluster resource creates an AWS PCS cluster.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-pcs.git",
  "definitions" : {
    "Accounting" : {
      "type" : "object",
      "description" : "The accounting configuration includes configurable settings for Slurm accounting.",
      "properties" : {
        "DefaultPurgeTimeInDays" : {
          "type" : "integer",
          "description" : "The default value for all purge settings for `slurmdbd.conf`. For more information, see the [slurmdbd.conf documentation at SchedMD](https://slurm.schedmd.com/slurmdbd.conf.html). The default value is `-1`. A value of `-1` means there is no purge time and records persist as long as the cluster exists.",
          "default" : -1,
          "minimum" : -1,
          "maximum" : 10000
        },
        "Mode" : {
          "type" : "string",
          "description" : "The default value is `STANDARD`. A value of `STANDARD` means that Slurm accounting is enabled.",
          "default" : "NONE",
          "enum" : [ "STANDARD", "NONE" ]
        }
      },
      "required" : [ "Mode" ]
    },
    "AuthKey" : {
      "type" : "object",
      "description" : "The shared Slurm key for authentication, also known as the cluster secret.",
      "properties" : {
        "SecretArn" : {
          "type" : "string",
          "description" : "The Amazon Resource Name (ARN) of the the shared Slurm key."
        },
        "SecretVersion" : {
          "type" : "string",
          "description" : "The version of the shared Slurm key."
        }
      },
      "required" : [ "SecretArn", "SecretVersion" ],
      "additionalProperties" : False
    },
    "Endpoint" : {
      "type" : "object",
      "description" : "An endpoint available for interaction with the scheduler.",
      "properties" : {
        "Port" : {
          "type" : "string",
          "description" : "The endpoint's connection port number."
        },
        "PrivateIpAddress" : {
          "type" : "string",
          "description" : "The endpoint's private IP address."
        },
        "Type" : {
          "type" : "string",
          "description" : "Indicates the type of endpoint running at the specific IP address.",
          "enum" : [ "SLURMCTLD", "SLURMDBD" ]
        },
        "PublicIpAddress" : {
          "type" : "string",
          "description" : "The endpoint's public IP address."
        }
      },
      "required" : [ "Port", "PrivateIpAddress", "Type" ],
      "additionalProperties" : False
    },
    "ErrorInfo" : {
      "type" : "object",
      "description" : "An error that occurred during resource provisioning.",
      "properties" : {
        "Code" : {
          "type" : "string",
          "description" : "The short-form error code."
        },
        "Message" : {
          "type" : "string",
          "description" : "The detailed error information."
        }
      },
      "additionalProperties" : False
    },
    "SecurityGroupId" : {
      "type" : "string",
      "description" : "A VPC security group ID."
    },
    "SlurmCustomSetting" : {
      "type" : "object",
      "description" : "Additional settings that directly map to Slurm settings.",
      "properties" : {
        "ParameterName" : {
          "type" : "string",
          "description" : "AWS PCS supports configuration of the following Slurm parameters for clusters: Prolog, Epilog, and SelectTypeParameters."
        },
        "ParameterValue" : {
          "type" : "string",
          "description" : "The value for the configured Slurm setting."
        }
      },
      "additionalProperties" : False,
      "required" : [ "ParameterName", "ParameterValue" ]
    },
    "SubnetId" : {
      "type" : "string",
      "description" : "A VPC subnet ID."
    },
    "Tag" : {
      "type" : "object",
      "description" : "A key-value pair to associate with a resource.",
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
      "additionalProperties" : False,
      "required" : [ "Key" ]
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : "The unique Amazon Resource Name (ARN) of the cluster."
    },
    "Endpoints" : {
      "type" : "array",
      "description" : "The list of endpoints available for interaction with the scheduler.",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Endpoint"
      }
    },
    "ErrorInfo" : {
      "type" : "array",
      "description" : "The list of errors that occurred during cluster provisioning.",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/ErrorInfo"
      }
    },
    "Id" : {
      "type" : "string",
      "description" : "The generated unique ID of the cluster.",
      "pattern" : "^(pcs_[a-zA-Z0-9]+|[A-Za-z][A-Za-z0-9-]{1,40})$"
    },
    "Name" : {
      "type" : "string",
      "description" : "The name that identifies the cluster."
    },
    "Networking" : {
      "type" : "object",
      "description" : "The networking configuration for the cluster's control plane.",
      "properties" : {
        "SecurityGroupIds" : {
          "type" : "array",
          "description" : "The list of security group IDs associated with the Elastic Network Interface (ENI) created in subnets.",
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/SecurityGroupId"
          }
        },
        "SubnetIds" : {
          "type" : "array",
          "description" : "The list of subnet IDs where AWS PCS creates an Elastic Network Interface (ENI) to enable communication between managed controllers and AWS PCS resources. The subnet must have an available IP address, cannot reside in AWS Outposts, AWS Wavelength, or an AWS Local Zone. AWS PCS currently supports only 1 subnet in this list.",
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/SubnetId"
          }
        }
      },
      "additionalProperties" : False
    },
    "Scheduler" : {
      "type" : "object",
      "description" : "The cluster management and job scheduling software associated with the cluster.",
      "properties" : {
        "Type" : {
          "type" : "string",
          "description" : "The software AWS PCS uses to manage cluster scaling and job scheduling.",
          "enum" : [ "SLURM" ]
        },
        "Version" : {
          "type" : "string",
          "description" : "The version of the specified scheduling software that AWS PCS uses to manage cluster scaling and job scheduling."
        }
      },
      "required" : [ "Type", "Version" ],
      "additionalProperties" : False
    },
    "Size" : {
      "type" : "string",
      "description" : "The size of the cluster.",
      "enum" : [ "SMALL", "MEDIUM", "LARGE" ]
    },
    "SlurmConfiguration" : {
      "type" : "object",
      "description" : "Additional options related to the Slurm scheduler.",
      "properties" : {
        "Accounting" : {
          "$ref" : "#/definitions/Accounting"
        },
        "AuthKey" : {
          "$ref" : "#/definitions/AuthKey"
        },
        "ScaleDownIdleTimeInSeconds" : {
          "type" : "integer",
          "description" : "The time before an idle node is scaled down.",
          "minimum" : 1
        },
        "SlurmCustomSettings" : {
          "type" : "array",
          "description" : "Additional Slurm-specific configuration that directly maps to Slurm settings.",
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/SlurmCustomSetting"
          }
        }
      },
      "additionalProperties" : False
    },
    "Status" : {
      "type" : "string",
      "description" : "The provisioning status of the cluster. The provisioning status doesn't indicate the overall health of the cluster.",
      "enum" : [ "CREATING", "ACTIVE", "UPDATING", "DELETING", "CREATE_FAILED", "DELETE_FAILED", "UPDATE_FAILED" ]
    },
    "Tags" : {
      "description" : "1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.",
      "patternProperties" : {
        "^.+$" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "required" : [ "Networking", "Scheduler", "Size" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Networking", "/properties/Scheduler", "/properties/Size", "/properties/SlurmConfiguration" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Endpoints", "/properties/ErrorInfo", "/properties/Id", "/properties/Status" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateNetworkInterface", "ec2:DescribeVpcs", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups", "ec2:GetSecurityGroupsForVpc", "iam:CreateServiceLinkedRole", "secretsmanager:CreateSecret", "secretsmanager:TagResource", "pcs:CreateCluster", "pcs:GetCluster", "pcs:ListTagsForResource", "pcs:TagResource" ],
      "timeoutInMinutes" : 60
    },
    "read" : {
      "permissions" : [ "pcs:GetCluster", "pcs:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "pcs:GetCluster", "pcs:ListTagsForResource", "pcs:TagResource", "pcs:UntagResource" ],
      "timeoutInMinutes" : 60
    },
    "delete" : {
      "permissions" : [ "pcs:DeleteCluster", "pcs:GetCluster" ],
      "timeoutInMinutes" : 60
    },
    "list" : {
      "permissions" : [ "pcs:ListClusters" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "pcs:TagResource", "pcs:ListTagsForResource", "pcs:UntagResource" ]
  }
}