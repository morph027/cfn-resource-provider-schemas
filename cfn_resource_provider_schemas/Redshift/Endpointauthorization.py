SCHEMA = {
  "tagging" : {
    "taggable" : False
  },
  "typeName" : "AWS::Redshift::EndpointAuthorization",
  "readOnlyProperties" : [ "/properties/Grantor", "/properties/Grantee", "/properties/AuthorizeTime", "/properties/ClusterStatus", "/properties/Status", "/properties/AllowedAllVPCs", "/properties/AllowedVPCs", "/properties/EndpointCount" ],
  "description" : "Describes an endpoint authorization for authorizing Redshift-managed VPC endpoint access to a cluster across AWS accounts.",
  "createOnlyProperties" : [ "/properties/ClusterIdentifier", "/properties/Account" ],
  "primaryIdentifier" : [ "/properties/ClusterIdentifier", "/properties/Account" ],
  "required" : [ "ClusterIdentifier", "Account" ],
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-redshift",
  "handlers" : {
    "read" : {
      "permissions" : [ "redshift:DescribeEndpointAuthorization" ]
    },
    "create" : {
      "permissions" : [ "redshift:AuthorizeEndpointAccess", "redshift:DescribeEndpointAuthorization" ],
      "timeoutInMinutes" : 60
    },
    "update" : {
      "permissions" : [ "redshift:AuthorizeEndpointAccess", "redshift:DescribeEndpointAuthorization", "redshift:RevokeEndpointAccess" ],
      "timeoutInMinutes" : 60
    },
    "list" : {
      "permissions" : [ "redshift:DescribeEndpointAuthorization" ]
    },
    "delete" : {
      "permissions" : [ "redshift:RevokeEndpointAccess", "redshift:DeleteEndpointAccess", "redshift:DescribeEndpointAuthorization", "ec2:DeleteClientVpnEndpoint", "ec2:DescribeVpcAttribute", "ec2:DescribeSecurityGroups", "ec2:DescribeAddresses", "ec2:DescribeInternetGateways", "ec2:DescribeSubnets" ],
      "timeoutInMinutes" : 60
    }
  },
  "writeOnlyProperties" : [ "/properties/Force" ],
  "additionalProperties" : False,
  "definitions" : {
    "VpcId" : {
      "relationshipRef" : {
        "typeName" : "AWS::EC2::VPC",
        "propertyPath" : "/properties/VpcId"
      },
      "pattern" : "^vpc-[A-Za-z0-9]{1,17}$",
      "type" : "string"
    },
    "AwsAccount" : {
      "pattern" : "^\\d{12}$",
      "type" : "string"
    }
  },
  "properties" : {
    "Status" : {
      "description" : "The status of the authorization action.",
      "type" : "string"
    },
    "Grantee" : {
      "description" : "The AWS account ID of the grantee of the cluster.",
      "$ref" : "#/definitions/AwsAccount"
    },
    "Account" : {
      "description" : "The target AWS account ID to grant or revoke access for.",
      "$ref" : "#/definitions/AwsAccount"
    },
    "Grantor" : {
      "description" : "The AWS account ID of the cluster owner.",
      "$ref" : "#/definitions/AwsAccount"
    },
    "EndpointCount" : {
      "description" : "The number of Redshift-managed VPC endpoints created for the authorization.",
      "type" : "integer"
    },
    "AuthorizeTime" : {
      "description" : "The time (UTC) when the authorization was created.",
      "type" : "string"
    },
    "AllowedVPCs" : {
      "description" : "The VPCs allowed access to the cluster.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/VpcId"
      }
    },
    "Force" : {
      "description" : " Indicates whether to force the revoke action. If True, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.",
      "type" : "boolean"
    },
    "AllowedAllVPCs" : {
      "description" : "Indicates whether all VPCs in the grantee account are allowed access to the cluster.",
      "type" : "boolean"
    },
    "VpcIds" : {
      "description" : "The virtual private cloud (VPC) identifiers to grant or revoke access to.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/VpcId"
      }
    },
    "ClusterIdentifier" : {
      "pattern" : "^(?=^[a-z][a-z0-9]*(-[a-z0-9]+)*$).{1,63}$",
      "description" : "The cluster identifier.",
      "type" : "string"
    },
    "ClusterStatus" : {
      "description" : "The status of the cluster.",
      "type" : "string"
    }
  }
}