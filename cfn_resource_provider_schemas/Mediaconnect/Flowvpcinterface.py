SCHEMA = {
  "typeName" : "AWS::MediaConnect::FlowVpcInterface",
  "description" : "Resource schema for AWS::MediaConnect::FlowVpcInterface",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-mediaconnect.git",
  "properties" : {
    "FlowArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow."
    },
    "Name" : {
      "type" : "string",
      "description" : "Immutable and has to be a unique against other VpcInterfaces in this Flow."
    },
    "RoleArn" : {
      "type" : "string",
      "description" : "Role Arn MediaConnect can assume to create ENIs in customer's account."
    },
    "SecurityGroupIds" : {
      "type" : "array",
      "description" : "Security Group IDs to be used on ENI.",
      "items" : {
        "type" : "string"
      }
    },
    "SubnetId" : {
      "type" : "string",
      "description" : "Subnet must be in the AZ of the Flow"
    },
    "NetworkInterfaceIds" : {
      "type" : "array",
      "description" : "IDs of the network interfaces created in customer's account by MediaConnect.",
      "items" : {
        "type" : "string"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "FlowArn", "Name", "RoleArn", "SubnetId", "SecurityGroupIds" ],
  "primaryIdentifier" : [ "/properties/FlowArn", "/properties/Name" ],
  "readOnlyProperties" : [ "/properties/NetworkInterfaceIds" ],
  "createOnlyProperties" : [ "/properties/FlowArn", "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:PassRole", "mediaconnect:DescribeFlow", "mediaconnect:AddFlowVpcInterfaces" ]
    },
    "read" : {
      "permissions" : [ "mediaconnect:DescribeFlow" ]
    },
    "update" : {
      "permissions" : [ "mediaconnect:DescribeFlow", "mediaconnect:AddFlowVpcInterfaces", "mediaconnect:RemoveFlowVpcInterface" ]
    },
    "delete" : {
      "permissions" : [ "mediaconnect:DescribeFlow", "mediaconnect:RemoveFlowVpcInterface" ]
    },
    "list" : {
      "permissions" : [ "mediaconnect:DescribeFlow" ]
    }
  }
}