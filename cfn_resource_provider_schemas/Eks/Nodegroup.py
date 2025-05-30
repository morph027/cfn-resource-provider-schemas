SCHEMA = {
  "typeName" : "AWS::EKS::Nodegroup",
  "description" : "Resource schema for AWS::EKS::Nodegroup",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "LaunchTemplateSpecification" : {
      "description" : "An object representing a launch template specification for AWS EKS Nodegroup.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Id" : {
          "type" : "string",
          "minLength" : 1
        },
        "Version" : {
          "type" : "string",
          "minLength" : 1
        },
        "Name" : {
          "type" : "string",
          "minLength" : 1
        }
      }
    },
    "Taint" : {
      "description" : "An object representing a Taint specification for AWS EKS Nodegroup.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1
        },
        "Value" : {
          "type" : "string",
          "minLength" : 0
        },
        "Effect" : {
          "type" : "string",
          "minLength" : 1
        }
      }
    },
    "ScalingConfig" : {
      "description" : "An object representing a auto scaling group specification for AWS EKS Nodegroup.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MinSize" : {
          "type" : "integer",
          "minimum" : 0
        },
        "DesiredSize" : {
          "type" : "integer",
          "minimum" : 0
        },
        "MaxSize" : {
          "type" : "integer",
          "minimum" : 1
        }
      }
    },
    "RemoteAccess" : {
      "description" : "An object representing a remote access configuration specification for AWS EKS Nodegroup.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SourceSecurityGroups" : {
          "type" : "array",
          "uniqueItems" : False,
          "insertionOrder" : False,
          "items" : {
            "type" : "string"
          }
        },
        "Ec2SshKey" : {
          "type" : "string"
        }
      },
      "required" : [ "Ec2SshKey" ]
    },
    "UpdateConfig" : {
      "description" : "The node group update configuration.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MaxUnavailable" : {
          "description" : "The maximum number of nodes unavailable at once during a version update. Nodes will be updated in parallel. This value or maxUnavailablePercentage is required to have a value.The maximum number is 100. ",
          "type" : "number",
          "minimum" : 1
        },
        "MaxUnavailablePercentage" : {
          "description" : "The maximum percentage of nodes unavailable during a version update. This percentage of nodes will be updated in parallel, up to 100 nodes at once. This value or maxUnavailable is required to have a value.",
          "type" : "number",
          "minimum" : 1,
          "maximum" : 100
        },
        "UpdateStrategy" : {
          "description" : "The configuration for the behavior to follow during an node group version update of this managed node group. You choose between two possible strategies for replacing nodes during an UpdateNodegroupVersion action.",
          "type" : "string"
        }
      }
    },
    "NodeRepairConfig" : {
      "description" : "The node auto repair configuration for node group.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Enabled" : {
          "description" : "Set this value to True to enable node auto repair for the node group.",
          "type" : "boolean"
        }
      }
    }
  },
  "properties" : {
    "AmiType" : {
      "description" : "The AMI type for your node group.",
      "type" : "string"
    },
    "CapacityType" : {
      "description" : "The capacity type of your managed node group.",
      "type" : "string"
    },
    "ClusterName" : {
      "description" : "Name of the cluster to create the node group in.",
      "type" : "string",
      "minLength" : 1
    },
    "DiskSize" : {
      "description" : "The root device disk size (in GiB) for your node group instances.",
      "type" : "integer"
    },
    "ForceUpdateEnabled" : {
      "description" : "Force the update if the existing node group's pods are unable to be drained due to a pod disruption budget issue.",
      "type" : "boolean",
      "default" : False
    },
    "InstanceTypes" : {
      "description" : "Specify the instance types for a node group.",
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Labels" : {
      "description" : "The Kubernetes labels to be applied to the nodes in the node group when they are created.",
      "type" : "object",
      "patternProperties" : {
        "^.+$" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "LaunchTemplate" : {
      "description" : "An object representing a node group's launch template specification.",
      "$ref" : "#/definitions/LaunchTemplateSpecification"
    },
    "NodegroupName" : {
      "description" : "The unique name to give your node group.",
      "type" : "string",
      "minLength" : 1
    },
    "NodeRole" : {
      "description" : "The Amazon Resource Name (ARN) of the IAM role to associate with your node group.",
      "type" : "string"
    },
    "ReleaseVersion" : {
      "description" : "The AMI version of the Amazon EKS-optimized AMI to use with your node group.",
      "type" : "string"
    },
    "RemoteAccess" : {
      "description" : "The remote access (SSH) configuration to use with your node group.",
      "$ref" : "#/definitions/RemoteAccess"
    },
    "ScalingConfig" : {
      "description" : "The scaling configuration details for the Auto Scaling group that is created for your node group.",
      "$ref" : "#/definitions/ScalingConfig"
    },
    "Subnets" : {
      "description" : "The subnets to use for the Auto Scaling group that is created for your node group.",
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Tags" : {
      "description" : "The metadata, as key-value pairs, to apply to the node group to assist with categorization and organization. Follows same schema as Labels for consistency.",
      "type" : "object",
      "patternProperties" : {
        "^.+$" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "Taints" : {
      "description" : "The Kubernetes taints to be applied to the nodes in the node group when they are created.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Taint"
      }
    },
    "UpdateConfig" : {
      "description" : "The node group update configuration.",
      "$ref" : "#/definitions/UpdateConfig"
    },
    "NodeRepairConfig" : {
      "description" : "The node auto repair configuration for node group.",
      "$ref" : "#/definitions/NodeRepairConfig"
    },
    "Version" : {
      "description" : "The Kubernetes version to use for your managed nodes.",
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "Arn" : {
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "eks:TagResource", "eks:UntagResource" ]
  },
  "required" : [ "ClusterName", "NodeRole", "Subnets" ],
  "createOnlyProperties" : [ "/properties/CapacityType", "/properties/NodegroupName", "/properties/RemoteAccess", "/properties/NodeRole", "/properties/ClusterName", "/properties/InstanceTypes", "/properties/DiskSize", "/properties/AmiType", "/properties/Subnets" ],
  "writeOnlyProperties" : [ "/properties/ForceUpdateEnabled" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "eks:CreateNodegroup", "eks:DescribeNodegroup", "eks:TagResource", "ec2:DescribeSubnets", "ec2:DescribeVpcs", "ec2:DescribeSecurityGroups", "ec2:DescribeKeyPairs", "ec2:CreateTags", "ec2:DeleteTags", "ec2:DescribeRouteTables", "ec2:DescribeLaunchTemplates", "ec2:DescribeLaunchTemplateVersions", "ec2:RunInstances", "iam:CreateServiceLinkedRole", "iam:GetRole", "iam:PassRole", "iam:ListAttachedRolePolicies" ]
    },
    "read" : {
      "permissions" : [ "eks:DescribeNodegroup" ]
    },
    "delete" : {
      "permissions" : [ "eks:DeleteNodegroup", "eks:DescribeNodegroup" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "ClusterName" : {
            "$ref" : "resource-schema.json#/properties/ClusterName"
          }
        },
        "required" : [ "ClusterName" ]
      },
      "permissions" : [ "eks:ListNodegroups" ]
    },
    "update" : {
      "permissions" : [ "iam:GetRole", "iam:PassRole", "eks:DescribeNodegroup", "eks:DescribeUpdate", "eks:ListUpdates", "eks:TagResource", "eks:UntagResource", "eks:UpdateNodegroupConfig", "eks:UpdateNodegroupVersion" ],
      "timeoutInMinutes" : 2160
    }
  }
}